from flask import Flask
import os
import logging

app = Flask(__name__)
UPLOAD_FOLDER = '/app/cargas'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

logging.basicConfig(level=logging.DEBUG)

from app.routes import cargar_archivo, descargar_archivo, eliminar_archivo

app.add_url_rule('/cargar', 'cargar_archivo', cargar_archivo, methods=['POST'])
app.add_url_rule('/descargar/<nombre_archivo>', 'descargar_archivo', descargar_archivo, methods=['GET'])
app.add_url_rule('/eliminar/<nombre_archivo>', 'eliminar_archivo', eliminar_archivo, methods=['DELETE'])
