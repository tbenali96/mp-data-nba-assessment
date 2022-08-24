import io
from typing import List
import pandas as pd
import uvicorn
from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel

from src.models.predict_model import predict_player_career

app = FastAPI()


class Prediction(BaseModel):
    filename: str
    content_type: str
    predictions: List[dict] = []


@app.get("/")
def root():
    return {"message": "Welcome to your NBA Players Classification API"}


@app.post("/predict")
async def prediction(file: UploadFile = File(...)):
    # Ensure that the file is a CSV
    if not file.content_type == "text/csv":
        raise HTTPException(status_code=400, detail="File provided is not a CSV file.")
    content = await file.read()
    data = pd.read_csv(io.BytesIO(content))
    print(data.head())
    response = predict_player_career(data, "../../models/random_forest_model.pkl", "../../models/scaler.pkl")
    # return the response as a JSON
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "predictions": tuple(response),
    }


if __name__ == "__main__":
    uvicorn.run("src.app.app:app --reload", host="127.0.0.1", port=8000)