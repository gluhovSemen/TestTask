#!flask/bin/python
from flask import Flask, jsonify, make_response, request
from flask import abort

app = Flask(__name__)
# создаю map машин и дилеров
cars = [
    {
        'id': 1,
        'brand': u'BMW',
        'description': u'Fast, expensive, luxury ',
        'sold': False
    },
    {
        'id': 2,
        'brand': u'Hundai',
        'description': u'Chip, durable',
        'sold': False
    }
]
salesmen = [
    {
        'id': 1,
        'name': u'Semen Glukhov',
        'work experience': 0,
        'salary': 1000
    },
    {
        'id': 2,
        'name': u'Dmitriy Erichev',
        'work experience': 10,
        'salary': 999999
    }
]

# обработка ошибок
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Bad reqest'}), 400)

# 4 GET по 2 на каждый класс
@app.route('/TestTask/api/v1.0/cars/<int:car_id>', methods=['GET'])
def get_car(car_id):
    car = list(filter(lambda t: t['id'] == car_id, cars))
    if len(car) == 0:
        abort(404)
    return jsonify({'car': car[0]})


@app.route('/TestTask/api/v1.0/salesmen/<int:salesman_id>', methods=['GET'])
def get_salesman(salesman_id):
    salesman = list(filter(lambda t: t['id'] == salesman_id, salesmen))
    if len(salesman) == 0:
        abort(404)
    return jsonify({'salesman': salesman[0]})


@app.route('/TestTask/api/v1.0/cars', methods=['GET'])
def get_cars():
    return jsonify({'cars': cars})


@app.route('/TestTask/api/v1.0/salesmen', methods=['GET'])
def get_salesmen():
    return jsonify({'salesmen': salesmen})

# Create для машин и дилеров
#для машины обязательный только бренд, продана или нет всегда fals
@app.route('/TestTask/api/v1.0/cars', methods=['POST'])
def create_car():
    if not request.json:
        abort(400)
    car = {
        'id': cars[-1]['id'] + 1,
        'brand': request.json['brand'],
        'description': request.json.get('description', ""),
        'sold': False
    }
    cars.append(car)
    return jsonify({'car': car}), 201

# для продовца все 3 поля обязательны
@app.route('/TestTask/api/v1.0/salesmen', methods=['POST'])
def create_salesman():
    if not request.json:
        abort(400)
    salesman = {
        'id': salesmen[-1]['id'] + 1,
        'name': request.json['name'],
        'work experience': request.json['work experience'],
        'salary': request.json.get('salary', "")

    }
    salesmen.append(salesman)
    return jsonify({'salesman': salesman}), 201

#Delete для обоих
@app.route('/TestTask/api/v1.0/cars/<int:car_id>', methods=['DELETE'])
def delete_car(car_id):
    car = list(filter(lambda t: t['id'] == car_id, cars))
    if len(car) == 0:
        abort(404)
    cars.remove(car[0])
    return jsonify({'result': True})


@app.route('/TestTask/api/v1.0/salesmen/<int:salesman_id>', methods=['DELETE'])
def delete_salesman(salesman_id):
    salesman = list(filter(lambda t: t['id'] == salesman_id, salesmen))
    if len(salesman) == 0:
        abort(404)
    salesmen.remove(salesman[0])
    return jsonify({'result': True})
# изменения для обоих
# для машины все параметры обязательны
@app.route('/TestTask/api/v1.0/cars/<int:car_id>', methods=['PUT'])
def update_car(car_id):
    car = list(filter(lambda t: t['id'] == car_id, cars))
    if len(car) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'sold' in request.json and type(request.json['sold']) is not bool:
        abort(400)
    car[0]['brand'] = request.json.get('brand', car[0]['brand'])
    car[0]['description'] = request.json.get('description', car[0]['description'])
    car[0]['sold'] = request.json.get('sold', car[0]['sold'])
    return jsonify({'car': car[0]})

# для продовца тоже все обязательные
@app.route('/TestTask/api/v1.0/salesmen/<int:salesman_id>', methods=['PUT'])
def update_salesman(salesman_id):
    salesman = list(filter(lambda t: t['id'] == salesman_id, salesmen))
    if len(salesman) == 0:
        abort(404)
    if not request.json:
        abort(400)
    salesman[0]['name'] = request.json.get('name', salesman[0]['name'])
    salesman[0]['work experience'] = request.json.get('work experience', salesman[0]['work experience'])
    salesman[0]['salary'] = request.json.get('salary', salesman[0]['salary'])
    return jsonify({'salesman': salesman[0]})


if __name__ == '__main__':
    app.run(debug=True)
