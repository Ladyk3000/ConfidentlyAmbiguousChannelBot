import time
import config
import os
import openai


class ChatGPT:
    def __init__(self):
        openai.api_key = config.OPENAI_API_KEY

    @staticmethod
    def get_post(query):
        openai.api_key = config.OPENAI_API_KEY
        response = openai.Completion.create(
            engine="davinci",
            prompt=query,
            temperature=0.3,
            max_tokens=64,
            top_p=1,
            frequency_penalty=0.5,
            presence_penalty=0)
        print(response)
        return response["choices"][0]["text"]
