from flask import jsonify, Flask, request
import os
from services_getway import ServicesGetway
from services import services

app = Flask(__name__)
servicesGetway = ServicesGetway(services)
port = os.environ.get("PORT", "6001")


@app.route('/', methods=['GET'])
def idnex():
    return jsonify({"status": True, "message": "server is running :)"})


@app.route('/services/call', methods=['POST'])
def register():
    data = request.json
    service_name = data["service_name"]
    endpoint = data["endpoint"]
    data = data["data"]

    app.logger.error("service_name", str(service_name))
    app.logger.error("endpoint", str(endpoint))
    app.logger.error("data", str(data))

    result = servicesGetway.call(service_name, endpoint, data)

    response = {
        **result
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run(port=port, host="0.0.0.0")
