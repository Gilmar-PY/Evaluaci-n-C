import cv2
import numpy as np
from multiprocessing import Pool

def apply_blur(segmento):
    print("Aplicando desenfoque al segmento")
    return cv2.GaussianBlur(segmento, (15, 15), 0)

def parallel_image_processing(ruta_imagen):
    print("Leyendo la imagen")
    imagen = cv2.imread(ruta_imagen)
    if imagen is None:
        raise FileNotFoundError(f"No se puede abrir el archivo de imagen: {ruta_imagen}")
    
    altura, anchura, _ = imagen.shape
    print(f"Dimensiones de la imagen: {anchura}x{altura}")

    print("Dividiendo la imagen en segmentos")
    segmentos = np.array_split(imagen, 4, axis=1)

    print("Procesando segmentos en paralelo")
    with Pool(processes=4) as pool:
        segmentos_desenfocados = pool.map(apply_blur, segmentos)

    print("Combinando los segmentos")
    imagen_desenfocada = np.hstack(segmentos_desenfocados)
    
    print("Guardando la imagen desenfocada")
    cv2.imwrite('imagen_desenfocada.jpg', imagen_desenfocada)

    print("Procesamiento completo")

parallel_image_processing('input_image.jpg')

