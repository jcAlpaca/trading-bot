from data import data
from models import model
from sklearn.metrics import accuracy_score

symbol = "AAPL"
df = data.get_data(symbol)

X, y = data.preprocess_data(df)

split_index = int(len(X) * 0.8)

X_train = X[:split_index]
X_test = X[split_index:]
y_train = y[:split_index]
y_test = y[split_index:]

classifier = model.XGBoostBinaryClassifier()

classifier.train(X_train, y_train)
y_pred = classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')
