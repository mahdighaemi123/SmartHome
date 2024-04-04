import pymongo

from bson.json_util import dumps
from bson.json_util import loads


class DataKeeper():

    def __init__(self, connection_string="mongodb://127.0.0.1:27017/Datakeeper", data_db="DataKeeper", data_collection="Data") -> None:
        self.client = pymongo.MongoClient(connection_string)
        self.db = self.client[data_db]
        self.data_collection = self.db[data_collection]

    def register_data(self, data):
        result = self.data_collection.insert_one(data)
        result = {
            "_id": str(result.inserted_id)
        }
        return result

    def retrive_data(self, query, sort=[("_id", -1)]):
        result = self.data_collection.find_one(query, sort=sort)

        if result is None:
            return None

        keys = list(result)

        result = {str(key): result[key] if isinstance(
            result[key], (str, int, float, dict, list)) else str(result[key]) for key in keys}
        return result

    def update_data(self, query, data):
        result = self.data_collection.update_one(query, data)

        result = {
            **result.raw_result
        }

        return result

    def delete_data(self, query):
        result = self.data_collection.delete_one(query)

        result = {
            **result.raw_result
        }

        return result
