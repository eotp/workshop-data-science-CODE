def model_matrix(data, y_col, x_col):
    if not isinstance(x_col, list):
        x_col = [x_col]
        
    # target vector shape (31,1)
    y = data[y_col].values.reshape(-1,1)
    print("Target vector y: {}".format(y.shape))

    # feature matrix shape (31,3)
    X = data.copy()
    X["beta0"]= 1
    X = X[["beta0"]+x_col].values
    print("Feature matrix X: {}".format(X.shape))    
    return X, y