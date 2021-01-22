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
    if isinstance(decoded_object, list):
        for task in decoded_object:
            todos.append(task) #agrega los objetos python a todos
    elif isinstance(decoded_object, dict):
        todos.append(decoded_object)
    else:
        return "bad input", 400
    return jsonify(todos) #jsonifica otra vez

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position) #borra el elemento
    # print("This is the position to delete: ",position)
    # return 'something'
    return jsonify(todos) #jsonifica la lista todos

#siempre deben ser las últimas líneas, de lo contrario estarían fuera de lo que lanza el servidor
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)

#pipenv run python src/app.py para correr este archivo
# el puerto 3245 se debe colocar publico para poder probar los métodos, sino da 401
#bc run -l python3 -g incremental correr el servidor de los ejercicios