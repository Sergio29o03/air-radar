# app/models/measurement.py
from pydantic import BaseModel
from typing import Dict
from datetime import datetime

class Concentration(BaseModel):
    value: float
    unit: str

class Measurement(BaseModel):
    Timestamp: datetime
    Humidity: float
    Temperature: float
    concentration_CO2: Concentration
    concentration_CO: Concentration
    concentration_NOX: Concentration
