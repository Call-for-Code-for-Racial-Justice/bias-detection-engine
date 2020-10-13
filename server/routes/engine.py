from flask import jsonify, request
from server import app

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from aif360.sklearn.metrics import disparate_impact_ratio, base_rate, consistency_score


def bias_table(Y, prot_attr=None, instance_type=None):
    groups = Y.index.unique(prot_attr)
    with np.errstate(divide='ignore', invalid='ignore'):
        pct = [Y.xs(g, level=prot_attr).shape[0]/Y.shape[0] for g in groups]
        data = [[np.divide(1, disparate_impact_ratio(Y[stage].dropna() == outcome, prot_attr=prot_attr, priv_group=g))
                 for stage in Y.columns for outcome in Y[stage].unique() if not pd.isna(outcome)]
                for g in groups]
    pct_name = 'proportion at first stage' if instance_type is None else f'proportion of {instance_type}'
    num_stages = len(data[0])
    col = pd.MultiIndex.from_tuples([(pct_name, '')]
            + list(zip(['disparate impact']*num_stages, [f'{stage} -> {outcome}' for stage in Y.columns for outcome in Y[stage].unique() if not pd.isna(outcome)])))
    table = pd.DataFrame(np.c_[pct, data], columns=col, index=groups).sort_index()
    table = filter_bias(table)
    def colorize(v):
        if v < 0.8:
            return 'color: red'
        elif v > 1.25:
            return 'color: blue'
        return ''
    return table.style.format('{:.3f}').format({(pct_name, ''): '{:.1%}'}
            ).bar(subset=pct_name, align='left', vmin=0, vmax=1, color='#5fba7d'
            ).applymap(colorize, subset='disparate impact')

def consistency_table(X, Y):
    data = [consistency_score(X.loc[Y[stage].notna()], Y[stage].dropna() == outcome)
            for stage in Y.columns for outcome in Y[stage].unique() if not pd.isna(outcome)]
    num_stages = len(data)
    col = pd.MultiIndex.from_tuples(list(zip(['consistency']*num_stages, [f'{stage} -> {outcome}' for stage in Y.columns for outcome in Y[stage].unique() if not pd.isna(outcome)])))
    table = pd.DataFrame([data], columns=col, index=['All Defendants'])
    table = filter_bias(table)
    def colorize(v):
        if v < 0.8:
            return 'color: red'
        return ''
    return table.style.format('{:.3f}').applymap(colorize)

def bias_grid(Y):
    num_stages = Y.columns.size - 1
    f, axes = plt.subplots(1, num_stages, figsize=(2+4*num_stages, 12), squeeze=True, sharey=True)
    for ax, stage, prev in zip(axes, Y.columns[1:], Y.columns):
        rates = Y[Y[prev]][stage].groupby(level=['race', 'gender']).apply(base_rate)
        sns.heatmap(rates.unstack(), annot=True, fmt='.1%', cmap='RdBu',
                    center=base_rate(Y[Y[prev]][stage]), robust=True,
                    cbar=False, square=True, ax=ax);
        ax.set_title(f'{prev} -> {stage}')
    plt.close()
    return f

def filter_bias(df):
    return df.loc[:, ((df < 0.8) | (df > 1.25)).any()]

def mean_difference(y_true, y_pred, prot_attr=None):
    unique = y_true.index.unique(prot_attr)
    groups = y_pred.index.get_level_values(prot_attr)
    data = [np.mean(y_pred[groups == g] - y_true[groups == g]) for g in unique]
    table = pd.DataFrame(data, columns=['Sentencing bias'], index=unique).sort_index()
    def colorize(v):
        if v > 0:
            return 'color: red'
        elif v < 0:
            return 'color: blue'
        return ''
    return table.style.format('{:.2f}').applymap(colorize)


@app.route('/sentencing-disparity', methods=['POST'])
def sentencing_disparity():
    data = request.json  # TODO: verify

    df = pd.read_csv('../data/simulated_data_v0.4.csv', index_col=0).set_index(['Case ID'])#, 'Race', 'Gender', 'Citizenship'])
    # fp = pd.concat([df.pop(c) for c in df.columns if c.startswith('FP')], axis=1)
    sent = pd.concat([df.pop(c) for c in df.columns[-5:]], axis=1)

    charge = df['Alleged Crime'] == data['charge_code']
    amount = df['Amount Range of Drug Possesed'] == data['controlled_substance_quantity_level']
    race = df['Race'] == data['race']
    gender = df['Gender'] == data['gender']

    sent = sent.loc[charge & amount & race & gender]
    if len(sent) < 10:
        return jsonify(message="Insufficient matching records exist in our "
                "database for this combination of charge, quantity, race, and "
                "gender."), 500

    prison = df['Sentencing'].str.contains('Prison', case=False, na=False)
    not_life = (sent['Estimated Sentence'] != 'life') & (sent['Given Sentence'] != 'life')
    sent = sent.loc[prison & not_life].astype(int)

    disparity = np.mean(sent['Given Sentence'] - sent['Estimated Sentence'])
    return jsonify(
        success=True,
        charge_code=data['charge_code'],
        race=data['race'],
        gender=data['gender'],
        controlled_substance_quantity_level=data['controlled_substance_quantity_level'],
        deviations=[dict(
                charge_code=data['charge_code'],
                sentence_deviations=[dict(
                        sentence_type='Prison Only',
                        commitmentTerm=disparity,
                        commitmentUnit="Months")])]
    )
