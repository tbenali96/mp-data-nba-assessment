import pandas as pd
from fastapi import FastAPI
from src.models.predict_model import predict

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Welcome to your NBA Players Classification API"}


@app.get("/predict_player_career")
def predict_player_career(payload):
    data = pd.DataFrame.from_dict(eval(payload))
    print(data)
    predictions = predict(data_for_prediction=data,
                          model_path="../../models/random_forest_model.pkl")
    return {"predictions": predictions}


'''
{"Name": ["Brandon Ingram"], "GP": [36], "MIN": [27.4], "PTS": [7.4],
                   "FGM": [2.6], "FGA": [7.6], "FG%": [34.7], "3P Made": [0.5], "3PA": [2.1],
                   "3P%": [25.0], "FTM": [1.6], "FTA": [2.3], "FT%": [69.9], "OREB": [0.7],
                   "DREB": [3.4], "REB": [4.1], "AST": [1.9], "STL": [0.4], "BLK": [0.4],
                   "TOV": [1.3]}
'''
