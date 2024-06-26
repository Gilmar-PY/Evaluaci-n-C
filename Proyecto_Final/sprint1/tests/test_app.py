import os
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_cargar_archivo(client):
    data = {
        'archivo': (open('test_file.txt', 'rb'), 'test_file.txt')
    }
    rv = client.post('/cargar', data=data)
    assert rv.status_code == 200
    assert b'Archivo cargado y cifrado exitosamente' in rv.data

def test_descargar_archivo(client):
    rv = client.get('/descargar/test_file.txt')
   
