# import la classe FastAPI dal modulo fastpi
from fastapi import FastAPI

# Creazione dell'istanza
app = FastAPI()

# Homepage
@app.get('/')
def root():
    return '''Benvenuto nella calcolatrice più inutile e inefficiente del web, per sapere la somma di due numeri digita nella barra dell'URL: <Home page URL>/num1/num2'''

# Somma di due numeri 
@app.get('/{num1}/{num2}')
def sum(num1 : int, num2 : int):
    '''restituisce a schermo la somma di due numeri'''

    return num1 + num2

