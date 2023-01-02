from flask import Flask, request, json, Response
from database import MongoAPI
import os

app = Flask(__name__)

@app.route('/health')
def base():
    return Response(response=json.dumps({"Status": "UP"}),
                    status=200,
                    mimetype='application/json')
  

@app.route('/', methods=['GET', 'POST'])
def log_in():
    username = request.args.get('user', default = "no_user", type = str)
    password = request.args.get('password', default = "no_password", type = str)
    document =  {
                    "user": username,
                    "password": password
                } 
    data = {
        "database": "admin",
        "collection": "usuarios",
    }
    database_obj = MongoAPI(data)
    response = database_obj.log_in_user(document)
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')
    

    
if __name__ == "__main__":
    if os.getenv("FLASK_ENV") == "development":
        app.run(debug=True)
    else:
        app.run(debug=False)