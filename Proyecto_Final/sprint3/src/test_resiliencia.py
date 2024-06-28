
import requests

def simular_fallo_nodo(nodo):
    try:
        response = requests.post(f"{nodo}/fallo")
        if response.status_code == 200:
            print(f"Fallo simulado exitosamente en {nodo}")
        else:
            print(f"Error simulando fallo en {nodo}")
    except Exception as e:
        print(f"Error: {e}")

def verificar_recuperacion_datos(nodo, archivo):
    try:
        response = requests.get(f"{nodo}/descargar/{archivo}")
        if response.status_code == 200:
            print(f"Recuperación de datos exitosa desde {nodo}")
        else:
            print(f"Error recuperando datos desde {nodo}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    simular_fallo_nodo("http://storage-node-2:5000")
    verificar_recuperacion_datos("http://storage-node-1:5000", "Actividad.txt")
