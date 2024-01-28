from flask import Flask, request, jsonify
from pymongo import MongoClient
import os
import time

app = Flask(__name__)

MONGO_URI = os.getenv("MONGO_URI")

mongo_client = MongoClient(MONGO_URI)
db = mongo_client["SmartHome"]

@app.route('/new_data', methods=['POST'])
def create_new_data():
    data = request.get_json(force=True)

    name = data.get("name")
    is_raining = data.get("is_raining")
    temp = data.get("temp")
    humidity = data.get("humidity")
    timestamp = time.time()

    collection = db[name]

    print({
        "name": name,
        "is_raining": is_raining,
        "temp": temp,
        "humidity": humidity,
        "timestamp":timestamp
    })

    collection.insert_one({
        "name": name,
        "is_raining": is_raining,
        "temp": temp,
        "humidity": humidity,
        "timestamp": timestamp,
    })

    return jsonify({"status": True, "message": "data saved :)"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)