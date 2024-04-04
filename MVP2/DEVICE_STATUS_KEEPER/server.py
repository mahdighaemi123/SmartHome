from flask import Flask, request, jsonify
import os
from device_status_keeper import ServiceStateKeeper
from services_getway import ServicesGetway

import time

app = Flask(__name__)
port = os.environ.get("PORT", "6008")

connection_string = os.environ.get(
    "GETWAY", "http://127.0.0.1:6001/")

getway = ServicesGetway(connection_string)


dataKeeper = ServiceStateKeeper(
    getway=getway,
)


@app.route('/', methods=['GET'])
def idnex():
    return jsonify({"status": True, "message": "server is running :)"})


@app.route('/device_status/register', methods=['POST'])
def register():
    data = request.json
    source_name = data["source_name"]
    service_name = data["service_name"]
    device_status = data["device_status"]
    timestamp = time.time()

    result = dataKeeper.register_device_status(
        source_name=source_name,
        service_name=service_name,
        device_status=device_status,
        timestamp=timestamp
    )

    response = {
        **result
    }

    return jsonify(response)


if __name__ == '__main__':
    app.run(port=port, host="0.0.0.0")
