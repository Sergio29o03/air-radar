from flask import Flask, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # Habilitar CORS para toda la aplicación 
# Ruta para obtener los datos del archivo JSON
@app.route('/data')

def get_data():
    try:
        with open('datos.json', 'r') as file:
            data = json.load(file)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({'error': 'El archivo JSON no existe'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
