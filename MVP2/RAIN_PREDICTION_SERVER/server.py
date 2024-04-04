from flask import Flask, request, jsonify
import os
from predict import PredictRainStatus

app = Flask(__name__)
port = os.environ.get("PORT", "6002")

predictRainStatus = PredictRainStatus()


@app.route('/', methods=['GET'])
def idnex():
    return jsonify({"status": True, "message": "server is running :)"})


@app.route('/rain_status/predict', methods=['POST'])
def predict():
    data = request.json

    data = {"Humidity9am": [data["humidity_9am"]],
            "Temp9am": [data["temp_9am"]],
            "RainToday": [data["rain_today"]]}

    prediction = predictRainStatus.predict(data)[0]

    response = {
        "staus": True,
        "message": "ok",
        "rain_status_prediction": True if prediction >= 50 else False,
        "score": prediction
    }

    return jsonify(response)


if __name__ == '__main__':
    app.run(port=port, host="0.0.0.0")
