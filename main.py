from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/suma', methods=['POST'])
def suma():
    data = request.get_json()

    if not ('numero_1' in data and 'numero_2' in data):
        return jsonify({"error": "Debes ingresar ambos campos"})
    
    numero_1 = data['numero_1']
    numero_2 = data['numero_2']

    try:
        numero_1 = int(data['numero_1'])
        numero_2 = int(data['numero_2'])
    except ValueError:
        return jsonify({"error": "Debes ingresar números"})
    
    resultado = numero_1 + numero_2
    
    return jsonify({"suma": + resultado})

@app.route('/resta', methods=['POST'])
def resta():
    data = request.get_json()

    if not ('numero_1' in data and 'numero_2' in data):
        return jsonify({"error": "Debes ingresar ambos campos"})
    
    numero_1 = data['numero_1']
    numero_2 = data['numero_2']

    try:
        numero_1 = int(data['numero_1'])
        numero_2 = int(data['numero_2'])
    except ValueError:
        return jsonify({"error": "Debes ingresar números"})
    
    resultado = numero_1 - numero_2

    return jsonify({"resta": + resultado})

@app.route('/multiplicacion', methods=['POST'])
def multiplicacion():
    data = request.get_json()

    if not ('numero_1' in data and 'numero_2' in data):
        return jsonify({"error": "Debes ingresar ambos campos"})
    
    numero_1 = data['numero_1']
    numero_2 = data['numero_2']
    
    try:
        numero_1 = int(data['numero_1'])
        numero_2 = int(data['numero_2'])
    except ValueError:
        return jsonify({"error": "Debes ingresar números"})
    
    resultado = numero_1 * numero_2

    return jsonify({"multiplicacion": + resultado})

@app.route('/division', methods=['POST'])
def division():
    data = request.get_json()

    if not ('numero_1' in data and 'numero_2' in data):
        return jsonify({"error": "Debes ingresar ambos campos"})
    
    numero_1 = data['numero_1']
    numero_2 = data['numero_2']
    
    try:
        numero_1 = int(data['numero_1'])
        numero_2 = int(data['numero_2'])
    except ValueError:
        return jsonify({"error": "Debes ingresar números"})
    
    resultado = numero_1 / numero_2

    return jsonify({"division": + resultado})

if __name__ == '__main__':
    app.run(debug=True)