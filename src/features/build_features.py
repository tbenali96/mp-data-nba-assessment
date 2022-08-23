import logging
import pickle
from pickle import dump
import pandas as pd
from sklearn.preprocessing import StandardScaler

IRRELEVANT_COLUMNS = ['Name']
CORRELATED_COLUMNS_TO_DROP = ['PTS', 'FGM', 'FGA', 'FTA', '3PA', 'OREB']
TARGET_COLUMN = ['TARGET_5Yrs']


def remove_irrelevant_columns(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    return df.drop(columns=columns)


def fill_na_with_mean(df: pd.DataFrame, col_with_nan_values: str) -> pd.DataFrame:
    df[col_with_nan_values] = df[col_with_nan_values].fillna(df[col_with_nan_values].mean())
    return df


def build_features(raw_data: pd.DataFrame, train_or_test: str) -> pd.DataFrame:
    data = remove_irrelevant_columns(raw_data, columns=IRRELEVANT_COLUMNS)
    data = fill_na_with_mean(data, col_with_nan_values='3P%')
    data = remove_irrelevant_columns(data, columns=CORRELATED_COLUMNS_TO_DROP)
    if train_or_test == 'train':
        features = data.drop(columns=TARGET_COLUMN)
        numeric_columns = features.select_dtypes(['int64', 'float64']).columns
        scaler = StandardScaler()
        scaler.fit(data[numeric_columns])
        dump(scaler, open('../../models/scaler.pkl', 'wb'))
    if train_or_test == 'test':
        numeric_columns = data.select_dtypes(['int64', 'float64']).columns
        with open('../../models/scaler.pkl', 'rb') as f:
            scaler = pickle.load(f)
    data[numeric_columns] = scaler.transform(data[numeric_columns])
    return data


if __name__ == '__main__':
    raw = pd.read_csv("../../data/raw/nba_logreg.csv")
    logging.info("Building the features")
    preprocessed_data = build_features(raw_data=raw, train_or_test="train")
    logging.info("Feature Engineering done")
    preprocessed_data.to_csv("../../data/processed/processed_data.csv", index=False)


