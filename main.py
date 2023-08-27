from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/suma', methods=['POST'])
def suma():
    data = request.get_json()
    numero_1 = data['numero_1']
    numero_2 = data['numero_2']
    resultado = numero_1 + numero_2

    return jsonify({"suma": + resultado})

@app.route('/multiplicacion', methods=['POST'])
def multiplicacion():
    data = request.get_json()
    numero_1 = data['numero_1']
    numero_2 = data['numero_2']
    resultado = numero_1 * numero_2

    return jsonify({"multiplicacion": + resultado})

if __name__ == '__main__':
    app.run(debug=True)