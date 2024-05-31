#Ejercicio 8: Evaluación de modelos en paralelo con joblib

#Descripción: Implementa un sistema para evaluar varios modelos de machine learning en paralelo utilizando joblib.

#Tareas:

 #   Entrenar varios modelos de machine learning con diferentes parámetros.
  #  Usar joblib.Parallel para evaluar los modelos en paralelo.
   # Comparar los resultados y seleccionar el mejor modelo.

#Pistas:

 #   Usa joblib.Parallel y joblib.delayed para paralelizar la evaluación de los modelos. Usa una métrica de evaluación adecuada, como la precisión o el F1-score.
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from joblib import Parallel, delayed

# Crea y entrena un modelo RandomForest con n_estimators árboles
def evaluate_model(n_estimators, X_train, X_test, y_train, y_test):
    model = RandomForestClassifier(n_estimators=n_estimators)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)##predice las etiquetas
    return (n_estimators, accuracy_score(y_test, y_pred))

def parallel_model_evaluation():
 #carga los datos iris
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=42)
    n_estimators_list = [10, 50, 100, 200]
    results = Parallel(n_jobs=4)(delayed(evaluate_model)(n, X_train, X_test, y_train, y_test) for n in n_estimators_list)
    return results

results = parallel_model_evaluation()
print(results)
