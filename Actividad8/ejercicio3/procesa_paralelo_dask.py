
#Ejercicio 3: Procesamiento paralelo de archivos con Dask
#Descripción: Utiliza Dask para procesar un conjunto de archivos CSV en paralelo, realizando una agregación (por ejemplo, promedio de una columna específica).
#Tareas:
#    Leer varios archivos CSV con Dask.
#    Procesar los archivos en paralelo para calcular el promedio de una columna específica.
#    Combinar los resultados y obtener el promedio total.
#Pistas:
#   Usa dask.dataframe.read_csv para leer los archivos.
#    Usa dask.dataframe para realizar las operaciones en paralelo.

import dask.dataframe as dd

def parallel_csv_processing(file_paths):
    df = dd.read_csv(file_paths)
    average_value = df['target_column'].mean().compute()
    return average_value

file_paths = ['file1.csv', 'file2.csv', 'file3.csv', 'file4.csv']
average = parallel_csv_processing(file_paths)
print(f"Average value: {average}")

