import pandas as pd
import numpy as np
import random

def weighted_data(r, black_stage_weights, black_sentencing_weights, other_sentencing_weights):
    """
    r: r is the size of the dataframe you want to generate
    black_stage_weights: weights for Race == Black, for Stage of Legal Procedure column (4 weights)
    black_sentencing_weights: weights for Race == Black, for Sentencing column (6 weights)
    other_sentencing_weights: weights for Race != Black, for Sentencing column (6 weights)

    For weight number use the follow 5,10,15,20,25,30,35,40,45,50
    The higher the number the more chance that the item will be picked.


    Weight Explained:
    Probability = element_weight/ sum of all weights
    weight = [10,20,30,40,50]
    The total weight is 10+20+30+40+50 = 150

    List is [111, 222, 333, 444, 555]

    It returns 111 with probability 10/150 = 0.06
    It returns 222 with probability 20/150 = 0.13
    It returns 333 with probability 30/150 = 0.20
    It returns 444 with probability 40/150 = 0.26
    It returns 555 with probability 50/150 = 0.33
    """
    columns = ["Breaking&Entering", "Stated intent with partner", "Happened at night", "Elements of assault identified", "Elements of theft identified","Race","Stage of Legal Procedure", "Sentencing"]
    race = ["Black", "White", "Hispanic", "Other"]
    stage = ["Plea Bargaining", "Investigation", "Pre-Trial Motions", "Initial Hearing/Arraignment"]
    sentencing = [0,1,2,3,4,5]
    df = pd.DataFrame(columns=columns)

    r=r
    # Initiate df
    df = pd.DataFrame(np.random.choice([True, False],size=(r, len(columns))), columns=columns)

    df['Race'] = np.resize(random.choices(race, k=r),r)

    # Black
    k = len(df[df['Race'] == 'Black'])
    mask = df['Race'] == 'Black'
    df.loc[mask, 'Stage of Legal Procedure'] = np.resize(random.choices(stage, weights=(black_stage_weights), k=k),k)

    # All other
    for r in race[1:]:
        k = len(df[df['Race'] == r])
        mask = df['Race'] == r
        df.loc[mask, 'Stage of Legal Procedure'] = np.resize(random.choices(stage, k=k),k)

    # Black
    k = len(df[df['Race'] == 'Black'])
    mask = df['Race'] == 'Black'
    df.loc[mask, 'Sentencing'] = np.resize(random.choices(sentencing, weights=(black_sentencing_weights), k=k),k)

    # All other
    for r in race[1:]:
        k = len(df[df['Race'] == r])
        mask = df['Race'] == r
        df.loc[mask, 'Sentencing'] = np.resize(random.choices(sentencing, weights=(other_sentencing_weights), k=k),k)


    return df
