import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Dice Simulator!"

@app.route('/roll', methods=['GET'])
def roll_dice():
    return jsonify({"result": 6})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Default to port 5000 if PORT is not set
    app.run(host="0.0.0.0", port=port)
