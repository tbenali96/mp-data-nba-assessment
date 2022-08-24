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
        sample_filepath = "../../data/test/sample.csv"
        client = TestClient(app=app)

        # when
        response = client.post(
            "/predict", files={"file": ("filename", open(sample_filepath, "rb"), "text/csv")}
        )

        # then
        assert response.status_code == 200

    def test_predict_player_career_raise_exception_when_format_is_not_csv(self):
        # given
        sample_filepath = "../../requirements.txt"
        client = TestClient(app=app)

        # when
        response = client.post(
            "/predict", files={"file": ("filename", open(sample_filepath, "rb"), "text/plain")}
        )

        # then
        assert response.status_code == 400
        assert response.json() == {"detail": "File provided is not a CSV file."}
