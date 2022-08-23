import logging
import pandas as pd
from joblib import dump
from sklearn.ensemble import RandomForestClassifier


def train_model(dataframe: pd.DataFrame, target_column: str) -> RandomForestClassifier:
    X = dataframe.drop(columns=[target_column])
    y = dataframe[target_column]
    model = RandomForestClassifier(random_state=0,
                                   criterion="gini",
                                   min_samples_split=2,
                                   n_estimators=150,
                                   class_weight='balanced')
    model.fit(X, y)
    dump(model, '../../models/random_forest_model.pkl')
    return model


if __name__ == '__main__':
    data = pd.read_csv("../../data/processed/processed_data.csv")
    logging.info("Training ...")
    preprocessed_data = train_model(dataframe=data, target_column='TARGET_5Yrs')
    logging.info("Training done")
