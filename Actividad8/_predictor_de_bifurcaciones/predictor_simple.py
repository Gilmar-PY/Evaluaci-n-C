#6 . Implementa un programa en Python que simule un predictor de bifurcaciones simple. Use un historial para predecir si una bifurcación será tomada o no y ajuste las predicciones basadas en los resultados.


class BranchPredictor:
    def __init__(self):
        self.history = {}

    def predict(self, branch):
        return self.history.get(branch, False)

    def update(self, branch, taken):
        self.history[branch] = taken

def main():
    predictor = BranchPredictor()
    branches = [("branch1", True), ("branch2", False), ("branch1", False), ("branch2", True)]

    for branch, taken in branches:
        prediction = predictor.predict(branch)
        print(f"Predicted: {prediction}, Actual: {taken}")
        predictor.update(branch, taken)

if __name__ == "__main__":
    main()
