import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from src.models.train_model import train_model


def test_train_model():
    # given
    dataframe = pd.DataFrame(
        {
            'feature1': [1, 2, 3],
            'feature2': [5, 8, 10],
            'feature3': [2, 9, -1],
            'target': [0, 1, 1],
        }
    )
    # when
    model = train_model(dataframe=dataframe, target_column='target')

    # then
    assert isinstance(model, RandomForestClassifier)
