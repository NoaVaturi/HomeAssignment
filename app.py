from flask import Flask, request, jsonify
import os
import datetime

app = Flask(__name__)


SECRET_VALUE = os.getenv("SECRET_VALUE", "my_secret")
LOG_FILE = os.getenv("LOG_FILE", "success.log")

@app.route('/validate', methods=['POST'])
def validate():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400
        
    data = request.json
    user_input = data.get("value")

    if user_input == SECRET_VALUE:
        client_ip = request.remote_addr
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        try:
            with open(LOG_FILE, "a") as f:
                f.write(f"{timestamp} - Success: IP {client_ip}\n")
        except Exception as e:
            return jsonify({"status": "error", "message": f"Failed to write log: {str(e)}"}), 500
        
        return jsonify({"status": "success", "message": "Access granted"}), 200
    else:
        return jsonify({"status": "fail", "message": "Wrong secret"}), 403

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)