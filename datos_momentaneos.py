import json
from datetime import datetime, timedelta
import random

# Función para generar un timestamp en el formato especificado
def generate_timestamp(start_date, end_date, interval):
    timestamp = start_date
    while timestamp <= end_date:
        yield timestamp.strftime("%Y-%m-%d %H:%M:%S")
        timestamp += interval

# Función para generar un valor aleatorio dentro de un rango
def generate_random_value(min_value, max_value):
    return round(random.uniform(min_value, max_value), 1)

# Generar datos
start_date = datetime(2024, 3, 17, 0, 0, 0)
end_date = datetime(2024, 5, 29, 23, 59, 59)
interval = timedelta(minutes=1)
num_measurements = 20000

data = []
timestamps = generate_timestamp(start_date, end_date, interval)
for _ in range(num_measurements):
    timestamp = next(timestamps)
    humidity = generate_random_value(40, 70)
    temperature = generate_random_value(25, 32)
    concentration_CO2 = {"value": generate_random_value(1000, 2000), "unity": "ppm"}
    concentration_CO = {"value": generate_random_value(50, 100), "unity": "ppm"}
    concentration_NOX = {"value": generate_random_value(0.2, 0.7), "unity": "ppm"}
    
    measurement = {
        "Timestamp": timestamp,
        "Humidity": humidity,
        "Temperature": temperature,
        "concentration_CO2": concentration_CO2,
        "concentration_CO": concentration_CO,
        "concentration_NOX": concentration_NOX
    }
    data.append(measurement)

# Guardar datos en un archivo JSON
with open('mediciones.json', 'w') as file:
    json.dump(data, file, indent=2)

print("Archivo JSON generado con éxito.")
