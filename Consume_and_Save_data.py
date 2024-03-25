import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
import time

# Inicializa la aplicación Firebase con tus credenciales
cred = credentials.Certificate("air-radar-firebase.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://air-radar-default-rtdb.firebaseio.com/'
})

# Referencia a tu base de datos en tiempo real
ref = db.reference('/')

# Ruta donde se guardará el archivo JSON localmente
json_file_path = 'datos.json'

while True:
    try:
        # Consulta los datos de Realtime Database
        data = ref.get()
        
        # Lee los datos actuales del archivo JSON, si existe
        try:
            with open(json_file_path, 'r') as json_file:
                json_data = json.load(json_file)
        except FileNotFoundError:
            json_data = {}
        
        # Actualiza los datos de humedad y temperatura en el archivo JSON
        if 'Sensores' in data:
            sensores_data = data['Sensores']
            if 'Humedad' in sensores_data and 'Temperatura' in sensores_data:
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                if 'Mediciones' not in json_data:
                    json_data['Mediciones'] = []
                json_data['Mediciones'].append({
                    'Timestamp': timestamp,
                    'Humedad': sensores_data['Humedad'],
                    'Temperatura': sensores_data['Temperatura']
                })
        
        # Guarda los datos actualizados en el archivo JSON
        with open(json_file_path, 'w') as json_file:
            json.dump(json_data, json_file, indent=4)
        
        print("Datos de humedad y temperatura guardados correctamente en el archivo JSON.")

    except Exception as e:
        print("Error al consultar y guardar los datos:", str(e))
    
    # Espera 12 segundos antes de la próxima consulta
    time.sleep(12)
