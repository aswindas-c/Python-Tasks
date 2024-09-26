from pymongo import MongoClient

class MongoDBModel:

    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['falcon_db']
        self.collection = self.db['users']