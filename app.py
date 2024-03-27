from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime, timedelta
from fastapi.responses import JSONResponse

import json
import random

app = FastAPI()

# Define la estructura de los datos de las mediciones
class Medicion(BaseModel):
    Timestamp: str
    Humidity: float
    Temperature: float
    concentration_CO2: dict
    concentration_CO: dict
    concentration_NOX: dict

# Cargar datos del archivo JSON
def cargar_mediciones():
    try:
        with open('mediciones.json', 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return None
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Obtener una medición aleatoria del JSON
def obtener_medicion_aleatoria(mediciones):
    if not mediciones:
        raise HTTPException(status_code=404, detail="No data found")
    return random.choice(mediciones)

# Obtener mediciones dentro de un rango de fechas
def obtener_mediciones_en_rango(mediciones, fecha_inicio, fecha_fin):
    if not mediciones:
        raise HTTPException(status_code=404, detail="No data found")
    try:
        fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
        fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d")
        mediciones_en_rango = [medicion for medicion in mediciones 
                               if fecha_inicio <= datetime.strptime(medicion["Timestamp"], "%Y-%m-%d %H:%M:%S") <= fecha_fin]
        return mediciones_en_rango
    except ValueError:
        raise HTTPException(status_code=400, detail="Format of date incorrect, use the format 'YYYY-MM-DD'")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Ruta para obtener una medición aleatoria
@app.get("/get_medicion", response_model=Medicion)
def get_medicion_aleatoria():
    mediciones = cargar_mediciones()
    medicion_aleatoria = obtener_medicion_aleatoria(mediciones)
    return medicion_aleatoria


@app.get("/mediciones", response_model=List[Medicion])
def obtener_mediciones():
    try:
        with open('mediciones.json', 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return {"error": "El archivo JSON no existe"}
    except Exception as e:
        return {"error": str(e)}



# Ruta para obtener mediciones en un rango de fechas
@app.get("/mediciones_por_fecha", response_model=List[Medicion])
def get_mediciones_por_fecha(fecha_inicio: str, fecha_fin: str):
    mediciones = cargar_mediciones()
    mediciones_en_rango = obtener_mediciones_en_rango(mediciones, fecha_inicio, fecha_fin)
    return mediciones_en_rango

# Ruta de bienvenida
@app.get("/")
def read_root():
    return {"message": "Bienvenido a mi API"}

# Manejo de errores
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(status_code=exc.status_code, content={"message": exc.detail})

@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    return JSONResponse(status_code=500, content={"message": "Error interno del servidor"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

