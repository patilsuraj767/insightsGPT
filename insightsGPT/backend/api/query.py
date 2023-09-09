import requests
import json
from flask import request
from flask_restful import Resource

from insightsGPT.lib.chromadb import getDB


class Query(Resource):
    def post(self):
        db = getDB()
        json_data = request.get_json(force=True)
        query = json_data['query']
        context = db.search(
            query=query,
            search_type="mmr",
            k=1
        )

        payload = {
            "question": query,
            "context": context[0].page_content
        }

        res = requests.post("http://localhost:8080/v1/chat/completions", data=json.dumps(payload))

        return {'res': res.text}
