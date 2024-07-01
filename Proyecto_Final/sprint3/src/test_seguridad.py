oviedo@oviedo:~/Evaluaci-n-C/Proyecto_Final/sprint3/src$ cat test_seguridad.py 
from app.routes import cifrar_archivo, descifrar_archivo

def probar_cifrado_descifrado():
    data = b"Datos de prueba"
    nonce, tag, ciphertext = cifrar_archivo(data)
    descifrado = descifrar_archivo(nonce, tag, ciphertext)
    assert data == descifrado, "La prueba de cifrado y descifrado falló"

if __name__ == "__main__":
    probar_cifrado_descifrado()
    print("Prueba de cifrado y descifrado exitosa")

