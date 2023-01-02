from flask import Flask, request, json, Response
from database import MongoAPI
import os


app = Flask(__name__)

@app.route('/health')
def base():
    return Response(response=json.dumps({"Name": "API Sign In","Status": "UP"}),
                    status=200,
                    mimetype='application/json')
  
    
@app.route('/', methods=['POST'])
def sign_in():
    data = request.json
    if data is None or data == {}:
        return Response(response=json.dumps({"Error": "Please provide connection information"}),
                        status=400,
                        mimetype='application/json')
    if 'Document' not in data:
        return Response(response=json.dumps({"Error": "Please provide username and password"}),
                        status=400,
                        mimetype='application/json')
    database_obj = MongoAPI(data)
    response = database_obj.write(data)
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')
    

    
if __name__ == "__main__":
    if os.getenv("FLASK_ENV") == "development":
        app.run(debug=True)
    else:
        app.run(debug=False)