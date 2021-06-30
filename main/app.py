from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import requests

from prepare_data import Product, ProductUser

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@db/postgres"
CORS(app)

db = SQLAlchemy(app)


@app.route("/api/products")
def index():
    return jsonify(Product.query.all())


@app.route("/")
def home():
    return "Hello"


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5000)