from flask import Flask, request, jsonify
import os
from temp_intensity_keeper import TempKeeper
from services_getway import ServicesGetway
import time

app = Flask(__name__)
port = os.environ.get("PORT", "6005")

connection_string = os.environ.get(
    "GETWAY", "http://127.0.0.1:6001/")

getway = ServicesGetway(connection_string)

dataKeeper = TempKeeper(
    getway=getway,
)


@app.route('/', methods=['GET'])
def idnex():
    return jsonify({"status": True, "message": "server is running :)"})


@app.route('/temp/register', methods=['POST'])
def register():
    data = request.json
    source_name = data["source_name"]
    service_name = data["service_name"]
    temp = data["temp"]
    timestamp = time.time()

    result = dataKeeper.register_temp(
        source_name=source_name,
        service_name=service_name,
        temp=temp,
        timestamp=timestamp
    )

    response = {
        **result
    }
    return jsonify(response)


@app.route('/temp/retrive/last', methods=['POST'])
def retrive():
    temp = dataKeeper.retrive_last_temp()

    response = {
        "status": True,
        "message": "ok",
        "temp": temp
    }

    return jsonify(response)


if __name__ == '__main__':
    app.run(port=port, host="0.0.0.0")
