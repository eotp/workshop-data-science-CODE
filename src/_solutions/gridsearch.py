param_grid = {"max_depth": [1, 2, 4, 8, 16, 32],
              'max_features': [3, 6, 12, 24, 48, 96]}
grid_search = GridSearchCV(clf, param_grid=param_grid, 
                           scoring='roc_auc', return_train_score=True)

grid_search.fit(X_train, y_train)
print(grid_search)