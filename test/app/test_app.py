from fastapi.testclient import TestClient
from src.app.app import app


class TestAPI:
    def test_root_returns_the_right_message(self):
        # given
        client = TestClient(app=app)

        # when
        response = client.get("/")

        # then
        assert response.json() == {"message": "Welcome to your NBA Players Classification API"}

    def test_predict_player_career(self):
        # given
        client = TestClient(app=app)
        payload = {"Name": ["Brandon Ingram"], "GP": [36], "MIN": [27.4], "PTS": [7.4],
                   "FGM": [2.6], "FGA": [7.6], "FG%": [34.7], "3P Made": [0.5], "3PA": [2.1],
                   "3P%": [25.0], "FTM": [1.6], "FTA": [2.3], "FT%": [69.9], "OREB": [0.7],
                   "DREB": [3.4], "REB": [4.1], "AST": [1.9], "STL": [0.4], "BLK": [0.4],
                   "TOV": [1.3]}

        # when
        response = client.post("/predict_sentiment", json=payload)
        print(response)

        # then
        assert response.status_code == 200
        assert response.json() == {"predictions": [1]}

    def test_predict_player_career_raise_exception_when_the_data_is_not_in_the_right_format(self):
        # given
        client = TestClient(app=app)
        payload_with_missing_features = {"Name": ["Brandon Ingram"], "GP": [36], "MIN": [27.4], "PTS": [7.4],
                   "FGM": [2.6], "FGA": [7.6], "FG%": [34.7], "3P Made": [0.5], "3PA": [2.1],
                   "3P%": [25.0], "FTM": [1.6], "FTA": [2.3], "FT%": [69.9], "OREB": [0.7],
                   "DREB": [3.4], "REB": [4.1], "AST": [1.9], "STL": [0.4], "BLK": [0.4],
                   "TOV": [1.3]}

        # when
        response = client.get("/predict_sentiment", json=payload_with_missing_features)

        # then
        assert response.status_code == 400
        assert response.json() == {"detail": "The payload is not in the right format"}
