from flask import Flask, jsonify, request
from .models import pdts

def create_app():
    app = Flask(__name__)

    products = []


    @app.route("/api/v1/products", methods=['POST'])
    def post_a_product():
        data = request.get_json()
        product_id = len(products) +1
        name = data["name"]
        price = data["price"]
        stock = data["stock"]
        products.append(pdts(product_id, name, price, stock))
        return jsonify({"message": "Added the product"}), 201

    @app.route("/api/v1/products", methods=['GET'])
    def get_products():
        ans = []
        for product in products:
            ans.append(product.addpdts())
        return jsonify(ans), 200

    return app