from flask import Flask, request, jsonify
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods = ["GET"])
def index():
    return "Welcome to the base advanced excel workshop"

@app.route("/api/january", methods = ["POST"])
def monthly_data():
    if request.json["key"] == 1234:
        return jsonify("message: success, content: monthly content")
    else:
        return jsonify("message: sorry there was an err accessing your material")
    
@app.route("/api/2024", methods = ["POST"])
def yearly_data():
    if request.json["key"] == 1234:
        return jsonify("message: success, content: yearly content")
    else:
        return jsonify("message: sorry there was an err accessing your material")



if __name__ == "__main__":
    app.run(port=8080, debug=True)