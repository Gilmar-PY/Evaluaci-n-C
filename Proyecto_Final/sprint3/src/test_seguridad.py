# test_seguridad.py
import requests
from Crypto.Cipher import AES
import os

def test_acceso_sin_clave():
    # Intentar acceder a un archivo cifrado sin la clave
    archivo = 'Actividad.txt'
    url = 'http://localhost:5000/cargar'
    files = {'archivo': open(archivo, 'rb')}
    response = requests.post(url, files=files)
    
    if response.status_code == 200:
        print('Carga exitosa. Probando acceso sin clave...')
        
        # Intentar descargar y descifrar sin la clave adecuada
        url_descargar = f'http://localhost:5000/descargar/{archivo}'
        response = requests.get(url_descargar)
        
        if response.status_code == 200:
            with open('temp_' + archivo, 'wb') as file_enc:
                file_enc.write(response.content)
                
            with open('temp_' + archivo, 'rb') as file_enc:
                nonce = file_enc.read(16)
                tag = file_enc.read(16)
                ciphertext = file_enc.read()
            
            # Intentar descifrar con una clave incorrecta
            clave_incorrecta = b'Incorrect_Key_16'
            try:
                cipher = AES.new(clave_incorrecta, AES.MODE_EAX, nonce=nonce)
                data = cipher.decrypt_and_verify(ciphertext, tag)
                print('ERROR: El archivo fue descifrado con una clave incorrecta.')
            except ValueError:
                print('Prueba de seguridad exitosa: No se pudo descifrar el archivo con una clave incorrecta.')
        else:
            print('Error al descargar el archivo para la prueba de seguridad.')
    else:
        print('Error al cargar el archivo para la prueba de seguridad.')

if __name__ == "__main__":
    test_acceso_sin_clave()


