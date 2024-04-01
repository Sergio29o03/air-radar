from fastapi import APIRouter
from datetime import datetime
import random
from app.models.measurement import Measurement, Concentration 

router = APIRouter()

@router.get("/random-measurement", response_model=Measurement)
def get_random_measurement():
    return Measurement(
        Timestamp=datetime.now(),
        Humidity=random.uniform(20.0, 90.0),
        Temperature=random.uniform(-10.0, 35.0),
        concentration_CO2=Concentration(value=random.uniform(400.0, 1000.0), unit="ppm"),
        concentration_CO=Concentration(value=random.uniform(0.0, 10.0), unit="ppm"),
        concentration_NOX=Concentration(value=random.uniform(0.0, 50.0), unit="ppb")
    )
