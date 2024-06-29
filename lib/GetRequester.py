import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        url = self.url
        response = requests.get(url)
        return response.content
        pass

    def load_json(self):
        data = self.get_response_body()
        converted_data = json.loads(data)
        return converted_data
        pass