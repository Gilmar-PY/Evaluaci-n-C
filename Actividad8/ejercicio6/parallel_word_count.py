#Ejercicio 6: Procesamiento paralelo de archivos con concurrent.futures

#Descripción: Implementa un sistema para procesar múltiples archivos de texto en paralelo, donde cada archivo se lee y se realiza una operación de conteo de palabras.

#Tareas:

 #   Crear una lista de archivos de texto.
  #  Usar concurrent.futures.ThreadPoolExecutor para procesar los archivos en paralelo.
   # Contar las palabras en cada archivo y almacenar los resultados en un diccionario.

#Pistas:

import concurrent.futures
import os

def count_words_in_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    word_count = len(text.split())
    return (file_path, word_count)

def parallel_word_count(file_paths):
    results = {}
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_file = {executor.submit(count_words_in_file, file_path): file_path for file_path in file_paths}
        for future in concurrent.futures.as_completed(future_to_file):
            file_path = future_to_file[future]
            try:
                file_path, count = future.result()
                results[file_path] = count
            except Exception as exc:
                print(f"{file_path} generated an exception: {exc}")
    return results

file_paths = ["file1_long.txt", "file2_long.txt", "file3_long.txt"]
word_counts = parallel_word_count(file_paths)
print(word_counts)

