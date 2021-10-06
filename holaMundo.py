from flask import Flask

app = Flask(__name__) #nuevo objecto

@app.route('/') #wrap o decorador
def index(): 
    return 'Hola Mundo.' #regresar un string

app.run() #ejecutar el servidor 5000

