from flask import Flask
from flask_restful import Api

from api.v1.chat import Chat
from lib.config import LLM_API_PORT

app = Flask(__name__)
api = Api(app)

api.add_resource(Chat, '/v1/chat/completions')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=LLM_API_PORT, debug=True)
