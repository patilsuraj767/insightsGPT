from flask import request
from flask_restful import Resource
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from lib.config import LLM_MAX_NEW_TOKEN, LLM_MIN_LENGTH

model_name = "google/flan-t5-small"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)


class Chat(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        context = json_data['context']
        question = json_data['question']

        prompt_template = """Use the following pieces of context to answer the question at the end.
        If you don't know the answer, just say that you don't know, don't try to make up an answer.

        {context}

        Question: {question}
        Helpful Answer:""".format(context=context, question=question)

        inputs = tokenizer(prompt_template, return_tensors="pt")
        res = model.generate(**inputs, max_new_tokens=LLM_MAX_NEW_TOKEN, min_length=LLM_MIN_LENGTH)
        output = tokenizer.batch_decode(res, skip_special_tokens=True)

        return {'res': output}
