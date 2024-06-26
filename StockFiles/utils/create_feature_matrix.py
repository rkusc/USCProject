import pandas as pd

def create_feature_matrix(data, lags=[1, 2]):
    X = pd.DataFrame()
    for lag in lags:
        X[f'lag_{lag}'] = data['Close'].shift(lag)
    X = X.dropna()
    return X
