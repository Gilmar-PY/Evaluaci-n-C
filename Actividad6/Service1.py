from flask import Flask
import random

app = Flask(__name__)

@app.route('/random')
def random_number():
    """Genera un número aleatorio entre 1 y 100."""
    number = random.randint(1, 100)
    return {'number': number}

if __name__ == '__main__':
    app.run(port=5000) ## Cambia de puerto
