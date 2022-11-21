from flask import Flask, request, jsonify
from flask_cors import CORS
import util

app = Flask(__name__)

api_v1_cors_config = {"origins": ["http://localhost:5500"]}

CORS(app, resources={"/api/*": api_v1_cors_config})


@app.route("/", methods=["GET"])
def welcome():
    response = jsonify({"message": "Hello world"})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route("/api/get_location_names", methods=["GET"])
def get_location_names():
    response = jsonify({"locations": util.get_location_names()})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route("/api/predict_home_price", methods=["GET", "POST"])
def predict_home_price():
    total_sqft = float(request.form["total_sqft"])
    location = request.form["location"]
    bhk = int(request.form["bhk"])
    bath = int(request.form["bath"])

    response = jsonify(
        {"estimated_price": util.get_estimated_price(location, total_sqft, bhk, bath)}
    )
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == "__main__":
    util.load_saved_artifacts()
    app.run(port=5001)
