from date_time import DateTime
from flask import Flask, jsonify, request
import os

app = Flask(__name__)
port = os.environ.get("PORT", "6009")
dateTime = DateTime()


@app.route('/', methods=['GET'])
def idnex():
    return jsonify({"status": True, "message": "server is running :)"})


@app.route('/date_time/retrive', methods=['POST'])
def register():
    response = {
        "status": True,
        "message": "ok",
        "date_time": dateTime.get_date_time()
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run(port=port, host="0.0.0.0")
