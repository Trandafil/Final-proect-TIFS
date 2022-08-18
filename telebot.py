import json
import requests
import random
class TelegramBot:
    def __init__(self, pipeline):
        self.token = "5439894082:AAEvho76wly1aTAXwO4bui-U66A3UZplGNY"
        self.url = f"https://api.telegram.org/bot{self.token}"
        self.pipeline = pipeline

    def get_updates(self, offset=None):
        url = self.url + "/getUpdates?timeout=100"
        if offset:
            url = url + f"&offset={offset + 1}"
        url_info = requests.get(url)
        return json.loads(url_info.content)

    def sent_msg(self, msg, chat_id):
        url = self.url + f'/sendMessage?chat_id={chat_id}&text={msg}'
        if msg is not None:
            requests.get(url)

    def generate_response(self, user_text):
        pred = self.pipeline.predict([user_text])[0]
        if pred == "world":
            pred = 'You have entered world  category news'
        elif pred == "entertainment":
            pred = 'You have entered entertainment category news'
        elif pred == "sports":
            pred = 'This news from the world of sports'
        elif pred == "technology":
            pred = 'This news is technological'
        elif pred == "politics":
            pred = 'This political news'
        elif pred == "science":
            pred = 'This news from the field of science'
        elif pred == "automobile":
            pred = 'This news from automobile category'
        return pred






