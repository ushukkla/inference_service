from fastapi import FastAPI
from app.model import load_model, predict
from app.schemas import InputData, Prediction
import uvicorn

app = FastAPI()

model = load_model()

@app.post("/predict/", response_model=Prediction)
async def make_prediction(data: InputData):
    prediction = predict(model, data.features)
    return {"prediction": prediction}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
