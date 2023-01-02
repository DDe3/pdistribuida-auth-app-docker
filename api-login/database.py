from pymongo import MongoClient
import encrypt
import os

class MongoAPI:
    def __init__(self, data):
        cc = get_connection()
        self.client = MongoClient(cc)  
        database = data['database']
        collection = data['collection']
        cursor = self.client[database]
        self.collection = cursor[collection]
        self.data = data
        
    def log_in_user(self, data):
        query_json = {
            "user" : data['user']
        }
        documents = self.collection.find_one(query_json)
        if documents is None:
            return {'Status': 'Failure', "Message" : "User/Password incorrectos"}
        
        check = encrypt.verify_password(data['password'], documents['password'])
        
        if check:
            return {'Status': 'Success', "Message" : "User logged in"}
        else:
            return {'Status': 'Failure', "Message" : "User/Password incorrectos"}

    
    
def get_connection():
    MONGO_HOST = os.getenv("MONGO_HOST")
    MONGO_PORT = os.getenv("MONGO_PORT")
    MONGO_USERNAME = os.getenv("MONGO_USERNAME")
    MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
    cc = "mongodb://{}:{}@{}:{}/".format(MONGO_USERNAME,MONGO_PASSWORD,MONGO_HOST,MONGO_PORT)
    return cc