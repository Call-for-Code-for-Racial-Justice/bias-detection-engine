import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from aif360.sklearn.metrics import disparate_impact_ratio, base_rate


def bias_table(Y, prot_attr=None, instance_type=None):
    groups = Y.index.unique(prot_attr)
    with np.errstate(divide='ignore', invalid='ignore'):
        pct = [Y.xs(g, level=prot_attr).shape[0]/Y.shape[0] for g in groups]
        data = [[np.divide(1, disparate_impact_ratio(Y[Y[prev]][stage], prot_attr=prot_attr, priv_group=g))
                 for stage, prev in zip(Y.columns[1:], Y.columns)]
                for g in groups]
    num_stages = Y.columns.size - 1
    pct_name = 'proportion at first stage' if instance_type is None else f'proportion of {instance_type}'
    col = pd.MultiIndex.from_tuples([(pct_name, '')]
            + list(zip(['disparate impact']*num_stages, [f'{prev} -> {stage}' for stage, prev in zip(Y.columns[1:], Y.columns)])))
    table = pd.DataFrame(np.c_[pct, data], columns=col, index=groups).sort_index()
    def colorize(v):
        if v < 0.8:
            return 'color: red'
        elif v > 1.25:
            return 'color: blue'
        return ''
    return table.style.format('{:.3f}').format({(pct_name, ''): '{:.1%}'}
            ).bar(subset=pct_name, align='left', vmin=0, vmax=1, color='#5fba7d'
            ).applymap(colorize, subset='disparate impact')

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
