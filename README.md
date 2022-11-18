Prima di procedere con il progetto creo un ambiente virtuale tramite powershell<br>
<code> 
<path> python -m venv venv
</code><br><br>
Mi sposto nella cartella e attivo l'ambiente <br>
<code>
PS \<path> cd venv
</code>
<br>
<code>
PS \<path/venv> ./Scripts/Activate.ps1
</code><br><br>
Ora che l'ambiente è attivo, posso installare i packages che mi serviranno per il progetto <br>
<code>
(venv) PS <path/venv> pip install "fastapi[all]"
</code><br><br>
Torno indietro nella cartella di progetto<br>
<code>
    (venv) PS <path/venv> cd ../ 
</code><br><br>
Creo un file di testo con tutti i packages installati e le relative versioni<br>
<code>
(venv) PS \<path> pip freeze > requirements.txt
</code><br><br>


Creo il file main.py e copio il boilerplate della doc
<code>

    from fastapi import FastAPI

    app = FastAPI()


    @app.get("/")
    async def root():
        return {"message": "Hello World"}
</code><br>
Torno nel terminale e attivo il server
<br>
<code> 
(venv) PS \<path> uvicorn main:app --reload
</code><br><br>
Ora andando all'indirizzo <a href="http://127.0.0.1:8000"> http://127.0.0.1:8000</a> sarà possibile vedere il return della funzione root <br><br><br>
Il server è attivo, modifico il file main.py:<br><br>
Cambio la funzione root per dare una sorta di Homepage
<code>

    @app.get('/')
    def root():
        return '''Benvenuto nella calcolatrice più inutile e inefficiente del web, per sapere la somma di due numeri digita nella barra dell'URL: <root URL>/sum/num1/num2'''
</code>
E finalmente posso creare la mia funzione per avere la somma di due numeri
<code>

    @app.get('/sum/{num1}/{num2}')
    def sum(num1 : int, num2 : int):
    '''restituisce a schermo la somma di due numeri inseriti in un url di tipo root/sum/num1/num2'''

        return num1 + num2

</code>
Ho creato una funzione sum che prevede l'utilizzo di due parametri di tipo int e come return la loro somma
<code>@app.get('/sum/{num1}/{num2}')</code> è il decoratore della funzione che definisce l'url che prende i due numeri passati come input e li utilizza all'interno della funzione<br><br>
Creo infine un file .gitignore dove aggiungo i files che non voglio includere nel commit
<code>

    __pycache__
    venv
    .DS_Store
</code>

