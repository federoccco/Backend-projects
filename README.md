Prima di procedere con il progetto ho creato un ambiente virtuale tramite powershell
<br>
<code> 
    
    <path> python -m venv venv
</code>
<br>
Mi son spostato nella cartella e ho attivato l'ambiente 
<br>
<code>
    
    <path> cd venv
    <path/venv> ./Scripts/Activate.ps1
</code>
<br>
Ora che l'ambiente è attivo, posso installare i packages che mi serviranno per il progetto <br>
<code>
    
    <path/venv> pip3 install "fastapi[all]"
</code>
<br>
Torno indietro nella cartella di progetto
<br>
<code>
    
    <path/venv> cd ../ 
</code>
<br>
Creo il file main.py e copio il boilerplate della doc
<br>
<code>
    
    from fastapi import FastAPI

    app = FastAPI()


    @app.get("/")
    async def root():
        return {"message": "Hello World"}

</code>
Torno nel terminale e attivo il server
<br>
<code> 
    
    <path> uvicorn main:app --reload

</code>
<br>
Ora andando all'indirizzo <a href="http://127.0.0.1:8000"> http://127.0.0.1:8000</a> sarà possibile vedere il return della funzione root 
<br>
Ora che il server è attivo, modifico il file main.py
<br>
<br>
Cambio la funzione root per dare una sorta di Homepage
<code>

    @app.get('/')
    def root():
        return '''Benvenuto nella calcolatrice più inutile e inefficiente del web, per sapere la somma di due numeri digita nella barra dell'URL: <Home page URL>/num1/num2'''


</code>
<br>
E finalmente posso creare la mia funzione per avere la somma di due numeri
<code>

    @app.get('/{num1}/{num2}')
    def sum(num1 : int, num2 : int):
        return num1 + num2

</code>
Ho creato una funzione sum che prevede l'utilizzo di due parametri di tipo int e come return la loro somma <br>
<code>@app.get('/{num1}/{num2}')</code> è il decoratore della funzione che definisce l'url che prende i due numeri passati come input e li utilizza all'interno della funzione
<br>
<br>
Creo infine un file .gitignore dove aggiungo i files che non voglio nel commit
<code>
    
    __pycache__
    venv
    .DS_Store

</code>

