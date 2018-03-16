## selected functions 

import numpy as np
import pandas as pd

def train_test_split(df, ratio=0.3, rs=42):
    np.random.seed(rs)
    idx = np.random.choice([True, False], size=df.shape[0], 
                           replace=True, p=[1-ratio, ratio])
    train = df.loc[idx,:]
    test = df.loc[~idx,:]
    print("Train set: {}".format(train.shape))
    print("Test set: {}".format(test.shape))
    return train, test

def one_step_learning(X, y):
    return np.dot( np.dot ( np.linalg.inv ( np.dot(X.T, X) ), X.T), y )

def predict(X, beta):
    return np.dot(X, beta)

def rmse(y_hat, y):
    return np.sqrt(np.sum((y_hat-y)**2)/len(y))