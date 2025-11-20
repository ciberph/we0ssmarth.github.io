from flask import Flask, request, jsonify
from flask_cors import CORS
import csv
from datetime import datetime
 
app = Flask(__name__)
CORS(app)  # Esto permite solicitudes desde cualquier origen
 
# Ruta para guardar datos
@app.route('/guardar', methods=['POST'])
def guardar_datos():
    datos = request.json
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    archivo = f'datos_{timestamp}.csv'
    
    # Guardar en CSV
    with open(archivo, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(datos.keys())
        writer.writerow(datos.values())
    
    return jsonify({"status": "success", "archivo": archivo})
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
