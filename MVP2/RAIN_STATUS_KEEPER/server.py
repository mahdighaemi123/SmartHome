from flask import Flask, request, jsonify
import os
from rain_status_intensity_keeper import RainStatusKeeper
import time
from services_getway import ServicesGetway


app = Flask(__name__)
port = os.environ.get("PORT", "6007")

connection_string = os.environ.get(
    "GETWAY", "http://127.0.0.1:6001/")

getway = ServicesGetway(connection_string)

dataKeeper = RainStatusKeeper(
    getway=getway,
)


@app.route('/', methods=['GET'])
def idnex():
    return jsonify({"status": True, "message": "server is running :)"})


@app.route('/rain_status/register', methods=['POST'])
def register():
    data = request.json
    source_name = data["source_name"]
    service_name = data["service_name"]
    rain_status = data["rain_status"]
    timestamp = time.time()

    result = dataKeeper.register_rain_status(
        source_name=source_name,
        service_name=service_name,
        rain_status=rain_status,
        timestamp=timestamp
    )

    response = {
        **result
    }
    return jsonify(response)


@app.route('/rain_status/retrive/last', methods=['POST'])
def retrive():
    rain_status = dataKeeper.retrive_last_rain_status()

    response = {
        "status": True,
        "message": "ok",
        "rain_status": rain_status
    }

    return jsonify(response)


if __name__ == '__main__':
    app.run(port=port, host="0.0.0.0")
