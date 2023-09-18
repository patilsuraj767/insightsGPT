from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from insightsGPT.backend.api.query import Query

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(Query, '/query')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
