from pymongo import MongoClient
from urllib.parse import quote_plus
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
    
    def query_user(self, data):
        query_json = {
            "user" : data['user']
        }
        documents = self.collection.find_one(query_json)
        if documents is not None:
            return documents
        return None
        
    def write(self, data):
        new_document = data['Document']
        check_user = self.query_user(new_document)
        if check_user is not None:
            return {'Error': 'User ya existe'}
        new_document['password'] = encrypt.encrypt_password(new_document['password'])
        response = self.collection.insert_one(new_document)
        output = {'Status': 'Usuario registrado',
                  'Document_ID': str(response.inserted_id)}
        return output
    
    
    
def get_connection():
    MONGO_USERNAME = os.getenv("MONGO_USERNAME")
    MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
    MONGO_HOST = os.getenv("MONGO_HOST")
    MONGO_PORT = os.getenv("MONGO_PORT")
    cc = "mongodb://{}:{}@{}:{}/".format(MONGO_USERNAME,MONGO_PASSWORD,MONGO_HOST,MONGO_PORT)
    print(cc)
    return cc