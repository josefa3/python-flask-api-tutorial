from flask import Flask, jsonify, request, json #hay que importar jsonify

app = Flask(__name__) #instancia del servidor flask

# These two lines should always be at the end of your app.py file.
#url base
# if __name__ == '__main__':
#   app.run(host='0.0.0.0', port=3245, debug=True) #no recibe un endpoint, no hay nada que pedir aún, da 404

#endpoint

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET']) #endpoint que se añadirá
def hello_world():
    return jsonify(todos)

@app.route('/todos', methods=['POST']) #endpoint que se añadirá
def add_new_todo():
    request_body = request.data #data es una de las propiedades de request, json
    decoded_object = json.loads(request_body) #convierte en objeto python
    todos.append(decoded_object) #agrega los objetos python a todos
    print("Incoming request with the following body", request_body)
    return jsonify(todos) #jsonifica otra vez

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position) #borra el elemento
    # print("This is the position to delete: ",position)
    # return 'something'
    return jsonify(todos) #jsonifica la lista todos

# @app.route('/todos', methods=['GET', 'POST']) #endpoint que se añadirá
# def add_todo(): #esta funcion si debe ser distinto nombre, el endpoint puede ser igual
#     return jsonify(todos)

#siempre deben ser las últimas líneas, de lo contrario estarían fuera de lo que lanza el servidor
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)

#pipenv run python src/app.py para correr este archivo
#bc run -l python3 -g incremental correr el servidor de los ejercicios