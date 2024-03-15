import numpy as np
import pandas as pd
from utils import alpaca_api
from datetime import datetime, timedelta
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


def get_data(symbol, interval="1T", num_days=60):
    start_date = datetime.now() - timedelta(days=num_days)
    start_date = start_date.replace(hour=0, minute=0, second=0, microsecond=0)
    start_date = start_date.strftime('%Y-%m-%d')

    dfs = []

    for _ in range(num_days):
        bars_data = alpaca_api.get_bars(symbol, interval, start_date, 10000)['bars'][symbol]
        day_df = pd.DataFrame(bars_data)
        dfs.append(day_df)
        start_date = (datetime.strptime(start_date, '%Y-%m-%d') + timedelta(days=1)).strftime('%Y-%m-%d')

    combined_df = pd.concat(dfs, ignore_index=True)
    combined_df.drop_duplicates(subset=['t'], inplace=True)

    return combined_df


def preprocess_data(df, n_components=3, window_size=60):
    df['t'] = pd.to_datetime(df['t'])
    df.set_index('t', inplace=True)

    # Create labels
    df['next_close'] = df['c'].shift(-1)
    df['label'] = (df['next_close'] > df['c']).astype(int)
    df.drop('next_close', axis=1, inplace=True)
    df.dropna(inplace=True)

    # Normalize numerical features
    scaler = StandardScaler()
    numbers = df[['c', 'h', 'l', 'n', 'o', 'v', 'vw']]
    numbers = scaler.fit_transform(numbers)
    df[['c', 'h', 'l', 'n', 'o', 'v', 'vw']] = numbers

    # Prepare features for PCA
    X = df.drop('label', axis=1)

    # Perform PCA
    pca = PCA(n_components=n_components)
    pca.fit(X)
    pca_components = pca.transform(X)
    X_pca = pd.DataFrame(data=pca_components, columns=[f'PC{i + 1}' for i in range(n_components)])
    X_pca.index = X.index

    # Slide a window over your data to create the windowed dataset
    X_windowed = []
    y_windowed = []
    y = df['label']
    for i in range(len(X) - window_size):
        X_windowed.append(X_pca[i:i + window_size])
        y_windowed.append(y[i + window_size])

    # Convert lists to arrays
    X_windowed = np.array(X_windowed)
    y = np.array(y_windowed)
    X = X_windowed.reshape(X_windowed.shape[0], -1)

    return X, y

