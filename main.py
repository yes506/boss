from crypt import methods
from flask import Flask, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dataclasses import dataclass
import requests
from producer import publish

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@db/main'
CORS(app)

db = SQLAlchemy(app)

@dataclass
class Shop(db.Model):
    id: int
    shop_name: str
    shop_address: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    shop_name = db.Column(db.String(200))
    shop_address = db.Column(db.String(200))

@dataclass
class Order(db.Model):
    id: int
    shop: str
    address: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    shop = db.Column(db.Integer)
    address = db.Column(db.String(200))
    price = db.Column(db.Integer)

@dataclass
class Calc(db.Model):
    id: int
    shop: str
    price: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    shop = db.Column(db.Integer)
    price = db.Column(db.Integer)

@app.route('/api/shop')
def index():
    return jsonify(Shop.query.all())

@app.route('/api/calc', methods=['GET'])
def calc_list():
    return jsonify(Calc.query.all())

@app.route('/api/calc/sum/<int:shopId>')
def calc_sum(shopId):
    calc_list = Calc.query.filter_by(shop=shopId).all()
    sum = 0
    for calc in calc_list:
        sum += calc.price
    return jsonify({
        'message' : f'Shop {shopId} INCOME Total : {sum}won'
    })

@app.route('/api/calc/<int:orderId>', methods=['DELETE'])
def calc_delete(orderId):
    calc = Calc.query.get(orderId)
    db.session.delete(calc)
    db.session.commit()
    return jsonify({
       'message' : f'{orderId} order deleted' 
    })

@app.route('/api/order/<int:id>/deliver_finish', methods=['POST'])
def deliver_finish(id):
    publish('order_deliverfinished', id)
    return jsonify({
        'message' : f'{id} order delivery completed'
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')