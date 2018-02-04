'''
Helper functions for data science workshop
'''

import os
import numpy as np
import pandas as pd

PATH2DATA = os.path.abspath(os.path.join(os.getcwd(), os.pardir, 'datasets'))

def load_chicken():
    df = pd.read_csv(os.path.join(PATH2DATA, "chicken.csv"))
    chicken = pd.DataFrame(df.groupby(["Chick", "Diet"])["weight"].mean().round().astype(int)).reset_index()

    diets = chicken.groupby(["Diet", "Chick"])["weight"].mean().reset_index()
    chick_diet1 = diets.loc[diets["Diet"]==1, "weight"].values
    chick_diet2 = diets.loc[diets["Diet"] == 2, "weight"].values
    chick_diet3 = diets.loc[diets["Diet"] == 3, "weight"].values
    chick_diet4 = diets.loc[diets["Diet"] == 4, "weight"].values

    return chicken, chick_diet1, chick_diet2, chick_diet3, chick_diet4


def data_exponential(y0=2.5, m=-4.0, C=2.0, n=25):
    import numpy as np
    np.random.seed(1234)
    # Generate some data based on these
    x_min, x_max = 0, 1
    x = np.linspace(x_min, x_max, n)

    def model_func(x, y0, m, C):
        return y0 * np.exp(m * x) + C

    y = model_func(x, y0, m, C)
    # Add noise
    y = y + 0.75 * (np.random.random(n) - 0.5)

    return x, y