from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import uvicorn
import numpy as np
import pandas as pd

# Initialize FastAPI app
app = FastAPI()

# Define the input data model
class InputData(BaseModel):
    feature1: float
    feature2: float
    feature3: float
    feature4: float

# Load the trained machine learning model
try:
    with open("../models/random_forest_pipeline.pkl", "rb") as model_file:
        model = pickle.load(model_file)
except FileNotFoundError:
    raise Exception("Model file not found. Ensure 'trained_model.pkl' exists in the working directory.")

@app.post("/predict")
def predict(data: InputData):
    try:
        # Convert input data to a DataFrame for model compatibility
        input_df = pd.DataFrame([data.dict()])

        # Make predictions
        prediction = model.predict(input_df)

        # Format predictions
        result = {
            "prediction": prediction[0],
            "status": "success"
        }
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
