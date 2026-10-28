from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()
model = joblib.load("model.joblib")


class House(BaseModel):
    area: int
    bedrooms: int
    bathrooms: int
    stories: int
    mainroad: str
    guestroom: str
    basement: str
    hotwaterheating: str
    airconditioning: str
    parking: int
    prefarea: str
    furnishingstatus: str


@app.get("/")
def home():
    return {"message": "Housing API running"}


@app.post("/predict")
def predict(house: House):
    data = [[
        house.area,
        house.bedrooms,
        house.bathrooms,
        house.stories,
        house.mainroad,
        house.guestroom,
        house.basement,
        house.hotwaterheating,
        house.airconditioning,
        house.parking,
        house.prefarea,
        house.furnishingstatus
    ]]

    price = model.predict(data)[0]
    return {"predicted_price": round(float(price), 2)}