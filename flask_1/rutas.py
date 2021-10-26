from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index(): 
    return 'Hola Mundo.'

@app.route('/params')
def params(): 
    param = request.args.get('params1', 'No contiene este parametro.')
    param_dos = request.args.get('params2', 'No contiene este parametro.')
    return 'El parametro es {}, {}'.format(param, param_dos)

if __name__ == '__main__':
    app.run(debug = True, port= 8000)