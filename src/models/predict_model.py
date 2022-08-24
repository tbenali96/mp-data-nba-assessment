import logging
import numpy as np
import pandas as pd
from joblib import load
from src.features.build_features import build_features


def predict_player_career(data_for_prediction: pd.DataFrame, model_path: str, scaler_path: str) -> np.array:
    logging.info("Building the features for the test dataset")
    data = build_features(raw_data=data_for_prediction, train_or_test="test", scaler_path=scaler_path)
    logging.info("Feature Engineering done")
    model = load(model_path)
    return model.predict(data.values)


if __name__ == '__main__':
    test_data = pd.read_csv("../../data/test/sample.csv")
    logging.info("Predicting ...")
    predictions = predict_player_career(data_for_prediction=test_data,
                                        model_path="../../models/random_forest_model.pkl",
                                        scaler_path='../../models/scaler.pkl')
    logging.info("Prediction done")
    print(f'The results of your predictions are : {predictions}')