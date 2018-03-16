def train_test_split(df, ratio=0.3, rs=42):
    np.random.seed(rs)
    idx = np.random.choice([True, False], size=df.shape[0], 
                           replace=True, p=[1-ratio, ratio])
    train = df.loc[idx,:]
    test = df.loc[~idx,:]
    print("Train set: {}".format(train.shape))
    print("Test set: {}".format(test.shape))
    return train, test