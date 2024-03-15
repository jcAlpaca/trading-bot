from data import data

df = data.get_data("AAPL")
print(df.head())
X, y = data.preprocess_data(df)
X = X.reshape(X.shape[0], -1)
print(X.shape)
print(y.shape)