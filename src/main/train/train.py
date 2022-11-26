import joblib
import pandas as pd
import constants

from transformers import (CleanData,CreateCategoricalVariables,CreateDummies,SelectFeatures,MinMaxScaler)
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


categorical_process = Pipeline(
    steps=[
        ("create_variables", CreateCategoricalVariables()),
        ("get_dummies", CreateDummies(constants.CATEGORICAL_VARS)),
    ]
)

preprocessing = Pipeline(
    [
        ("clean", CleanData()),
        ("categorical_process", categorical_process),
        ("select_features", SelectFeatures(constants.FEATURES)),
        ("scaling", MinMaxScaler())
    ]
)

regression = LogisticRegression()

def train():

    titanic_pipeline = Pipeline(
        [
            ("preprocessing", preprocessing),
            ("logistic_regression", regression),
        ]
    )

    df = pd.read_csv(constants.URL).drop("home.dest", axis=1)

    X_train, X_test, y_train, y_test = train_test_split(
        df.drop(constants.TARGET, axis=1),
        df[constants.TARGET], 
        test_size=0.2, 
        random_state=2
    )

    titanic_pipeline.fit(X_train, y_train)

    preds = titanic_pipeline.predict(X_test)
    accuracy = (preds == y_test).sum() / len(y_test)
    print(f"Accuracy of the LogisticRegression model is {accuracy}")

    print(f"Model stored in {constants.PATH_MODEL}")
    joblib.dump(titanic_pipeline, f"{constants.PATH_MODEL}")


if __name__ == "__main__":
    train()