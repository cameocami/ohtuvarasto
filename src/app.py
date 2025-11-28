from flask import Flask, render_template, request, jsonify
from varasto import Varasto

app = Flask(__name__)

varastot = {}
counter = {'value': 0}


def parse_float(value, default=0.0):
    try:
        result = float(value)
        if result < 0:
            return default
        return result
    except (TypeError, ValueError):
        return default


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/varastot', methods=['GET'])
def get_varastot():
    result = []
    for varasto_id, varasto in varastot.items():
        result.append({
            'id': varasto_id,
            'tilavuus': varasto.tilavuus,
            'saldo': varasto.saldo,
            'paljonko_mahtuu': varasto.paljonko_mahtuu()
        })
    return jsonify(result)


@app.route('/api/varastot', methods=['POST'])
def create_varasto():
    data = request.get_json() or {}
    tilavuus = parse_float(data.get('tilavuus'))
    alku_saldo = parse_float(data.get('alku_saldo'))

    varasto = Varasto(tilavuus, alku_saldo)
    counter['value'] += 1
    varasto_id = counter['value']
    varastot[varasto_id] = varasto

    return jsonify({
        'id': varasto_id,
        'tilavuus': varasto.tilavuus,
        'saldo': varasto.saldo,
        'paljonko_mahtuu': varasto.paljonko_mahtuu()
    }), 201


@app.route('/api/varastot/<int:varasto_id>', methods=['PUT'])
def update_varasto(varasto_id):
    if varasto_id not in varastot:
        return jsonify({'error': 'Varasto not found'}), 404

    data = request.get_json() or {}
    tilavuus = parse_float(data.get('tilavuus'))
    alku_saldo = parse_float(data.get('alku_saldo'))

    varasto = Varasto(tilavuus, alku_saldo)
    varastot[varasto_id] = varasto

    return jsonify({
        'id': varasto_id,
        'tilavuus': varasto.tilavuus,
        'saldo': varasto.saldo,
        'paljonko_mahtuu': varasto.paljonko_mahtuu()
    })


@app.route('/api/varastot/<int:varasto_id>/lisaa', methods=['POST'])
def lisaa_varastoon(varasto_id):
    if varasto_id not in varastot:
        return jsonify({'error': 'Varasto not found'}), 404

    data = request.get_json() or {}
    maara = parse_float(data.get('maara'))

    varasto = varastot[varasto_id]
    old_saldo = varasto.saldo
    varasto.lisaa_varastoon(maara)
    added = varasto.saldo - old_saldo

    return jsonify({
        'id': varasto_id,
        'tilavuus': varasto.tilavuus,
        'saldo': varasto.saldo,
        'paljonko_mahtuu': varasto.paljonko_mahtuu(),
        'added': added
    })


@app.route('/api/varastot/<int:varasto_id>/ota', methods=['POST'])
def ota_varastosta(varasto_id):
    if varasto_id not in varastot:
        return jsonify({'error': 'Varasto not found'}), 404

    data = request.get_json() or {}
    maara = parse_float(data.get('maara'))

    varasto = varastot[varasto_id]
    taken = varasto.ota_varastosta(maara)

    return jsonify({
        'id': varasto_id,
        'tilavuus': varasto.tilavuus,
        'saldo': varasto.saldo,
        'paljonko_mahtuu': varasto.paljonko_mahtuu(),
        'taken': taken
    })


@app.route('/api/varastot/<int:varasto_id>', methods=['DELETE'])
def delete_varasto(varasto_id):
    if varasto_id not in varastot:
        return jsonify({'error': 'Varasto not found'}), 404

    del varastot[varasto_id]
    return jsonify({'success': True})


if __name__ == '__main__':
    import os
    debug_mode = os.environ.get('FLASK_DEBUG', 'false').lower() == 'true'
    app.run(debug=debug_mode)
