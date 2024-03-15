import xgboost as xgb
from sklearn.model_selection import train_test_split


class XGBoostBinaryClassifier:
    def __init__(self, n_estimators=100, max_depth=3, learning_rate=0.1, random_state=42):
        self.model = None
        self.n_estimators = n_estimators
        self.max_depth = max_depth
        self.learning_rate = learning_rate
        self.random_state = random_state

    def train(self, X_train, y_train):
        self.model = xgb.XGBClassifier(n_estimators=self.n_estimators,
                                       max_depth=self.max_depth,
                                       learning_rate=self.learning_rate,
                                       random_state=self.random_state)

        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        if self.model is None:
            raise Exception("Model has not been trained yet. Please train the model first.")
        return self.model.predict(X_test)

    def train_and_predict(self, X, y, test_size=0.2):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=self.random_state)
        self.train(X_train, y_train)
        y_pred = self.predict(X_test)
        return y_pred
