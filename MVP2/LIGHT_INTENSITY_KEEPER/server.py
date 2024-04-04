from flask import Flask, request, jsonify
import os
from light_intensity_keeper import LightIntensityKeeper
from services_getway import ServicesGetway
import time

app = Flask(__name__)
port = os.environ.get("PORT", "6004")

connection_string = os.environ.get(
    "GETWAY", "http://127.0.0.1:6001/")

getway = ServicesGetway(connection_string)

dataKeeper = LightIntensityKeeper(
    getway=getway,
)

@app.route('/', methods=['GET'])
def idnex():
    return jsonify({"status": True, "message": "server is running :)"})


@app.route('/light_intensity/register', methods=['POST'])
def register():
    data = request.json
    source_name = data["source_name"]
    service_name = data["service_name"]
    light_intensity = data["light_intensity"]
    timestamp = time.time()

    result = dataKeeper.register_light_intensity(
        source_name=source_name,
        service_name=service_name,
        light_intensity=light_intensity,
        timestamp=timestamp
    )

    response = {
        **result
    }
    return jsonify(response)


@app.route('/light_intensity/retrive/last', methods=['POST'])
def retrive():
    light_intensity = dataKeeper.retrive_last_light_intensity()

    response = {
        "status": True,
        "message": "ok",
        "light_intensity": light_intensity
    }

    return jsonify(response)


if __name__ == '__main__':
    app.run(port=port, host="0.0.0.0")
