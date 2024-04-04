from flask import Flask, request, jsonify
import os
from humidity_intensity_keeper import HumidityKeeper
from services_getway import ServicesGetway

import time
app = Flask(__name__)
port = os.environ.get("PORT", "6006")

connection_string = os.environ.get(
    "GETWAY", "http://127.0.0.1:6001/")

getway = ServicesGetway(connection_string)

dataKeeper = HumidityKeeper(
    getway=getway
)

@app.route('/', methods=['GET'])
def idnex():
    return jsonify({"status": True, "message": "server is running :)"})


@app.route('/humidity/register', methods=['POST'])
def register():
    data = request.json
    source_name = data["source_name"]
    service_name = data["service_name"]
    humidity = data["humidity"]
    timestamp = time.time()

    result = dataKeeper.register_humidity(
        source_name=source_name,
        service_name=service_name,
        humidity=humidity,
        timestamp=timestamp
    )

    response = {
        **result
    }
    return jsonify(response)


@app.route('/humidity/retrive/last', methods=['POST'])
def retrive():
    humidity = dataKeeper.retrive_last_humidity()

    response = {
        "status": True,
        "message": "ok",
        "humidity": humidity
    }

    return jsonify(response)


if __name__ == '__main__':
    app.run(port=port, host="0.0.0.0")
