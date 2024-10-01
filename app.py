from flask import Flask, request, jsonify

app = Flask(__name__)

# Main route
@app.route("/")
def home():
    return "Welcome to the Flask API Server!"

# Status route
@app.route("/status")
def status():
    return jsonify({"status": "Server is running", "version": "1.0.0"})

# Data route
@app.route("/data", methods=["POST"])
def data():
    data = request.json
    return jsonify({"received_data": data, "message": "Data received successfully!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
