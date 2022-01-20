from faculty import datasets
import mlflow
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def train():
    mlflow.set_experiment("ads")

    with mlflow.start_run():
        with datasets.open("Company_data.csv") as infile:
            ads = pd.read_csv(infile)

        X = ads['TV']
        y = ads['Sales']
    
        X_train_lm, X_test_lm, y_train_lm, y_test_lm = train_test_split(X, y)

        # Adding additional column to the train and test data
        X_train_lm = X_train_lm.values.reshape(-1,1)
        X_test_lm = X_test_lm.values.reshape(-1,1)

        model = LinearRegression()
        model.fit(X_train_lm, y_train_lm)

        # y = c + mX (or y = intercept + slope*X)
        print(f"intercept: {model.intercept_}")
        print(f"slope: {model.coef_}")
        mlflow.log_metric("intercept", model.intercept_)
        mlflow.log_metric("slope", model.coef_[0])

        # Log model to the registry
        mlflow.sklearn.log_model(model, "linear_regression_model")


if __name__ == "__main__":
    train()
