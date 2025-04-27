import os
import random
from flask import Flask, jsonify

app = Flask(__name__)

# Route for rolling a dice
@app.route('/roll', methods=['GET'])
def roll_dice():
    # Simulate rolling a 6-sided dice
    dice_roll = random.randint(1, 6)
    return jsonify({"result": dice_roll})

# Main entry point for the app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use Render's PORT variable or 5000 locally
    app.run(host="0.0.0.0", port=port)
