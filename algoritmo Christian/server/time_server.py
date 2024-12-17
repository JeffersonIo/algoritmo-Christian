from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/time', methods=['GET'])
def get_time():
    # Devuelve la hora actual en formato de timestamp
    current_time = datetime.utcnow().timestamp()
    return jsonify({"server_time": current_time})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
