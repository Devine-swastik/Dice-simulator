import os
from flask import Flask, request, jsonify

app = Flask(__name__)
API_KEY = "your-secret-api-key"

@app.route('/api/private', methods=['GET'])
def private_endpoint():
    if request.headers.get('Authorization') != f"Bearer {API_KEY}":
        return jsonify({"error": "Unauthorized"}), 401
    return jsonify({"message": "This is a private API endpoint!"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
