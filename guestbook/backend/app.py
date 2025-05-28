from flask import Flask, jsonify, request
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

data = []


@app.route('/api/messages', methods=['GET'])
def get_messages():
    return jsonify(data)


@app.route('/api/add_messages', methods=['POST'])
def add_message():
    message = request.json
    local_time = time.localtime()
    current_time = time.strftime('%d.%m.%Y г. %H:%M:%S', local_time)
    data_message = {
        'time': current_time[-8:],
        'name': message.get('name'),
        'message': message.get('message')
    }
    data.append(data_message)
    return data_message


if __name__ == '__main__':
    app.run(debug=True)
