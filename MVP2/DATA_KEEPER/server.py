from flask import Flask, request, jsonify
import os
from data_keeper import DataKeeper

app = Flask(__name__)
port = os.environ.get("PORT", "6003")
connection_string = os.environ.get(
    "MONGODB_CONNECTION_STRING", "mongodb://127.0.0.1:27017/Datakeeper")

dataKeeper = DataKeeper(
    connection_string=connection_string,
)


@app.route('/', methods=['GET'])
def idnex():
    return jsonify({"status": True, "message": "server is running :)"})


@app.route('/data/register', methods=['POST'])
def register():
    body = request.json
    data = body["data"]
    result = dataKeeper.register_data(data)

    response = {
        "staus": True,
        "message": "ok",
        "result": result
    }

    return jsonify(response)


@app.route('/data/retrive', methods=['POST'])
def retrive():
    body = request.json
    query = body["query"]
    sort = body.get("sort", [("_id", -1)])
    result = dataKeeper.retrive_data(query, sort=sort)

    response = {
        "staus": True,
        "message": "ok",
        "result": result
    }

    return jsonify(response)


@app.route('/data/update', methods=['POST'])
def update():
    query = request.json["query"]
    data = request.json["data"]
    result = dataKeeper.update_data(query, data)

    response = {
        "staus": True,
        "message": "ok",
        "result": result
    }

    return jsonify(response)


@app.route('/data/delete', methods=['POST'])
def delete():
    query = request.json
    result = dataKeeper.delete_data(query)

    response = {
        "staus": True,
        "message": "ok",
        "result": result
    }

    return jsonify(response)


if __name__ == '__main__':
    app.run(port=port, host="0.0.0.0")
