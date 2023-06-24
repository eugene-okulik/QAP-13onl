import requests
from endpoints.endpoint_handler import Endpoint


class GetUrlInfo(Endpoint):
    text = None
    __response_json = None

    def __init__(self, short_code, json_format=False):
        self.short_code = short_code
        self.json_format = json_format
        self.get_info()
        if self.json_format:
            self.code = self.__response_json['code']
            self.long_url = self.__response_json['long']

    def get_info(self):
        if self.json_format:
            response = requests.get(f'https://gotiny.cc/api/{self.short_code}?format=json')
            self.__response_json = response.json()
        else:
            response = requests.get(f'https://gotiny.cc/api/{self.short_code}')
        self.status_code = response.status_code
        self.text = response.text

    def response_text_contains_correct_url(self, long_url):
        return self.text == long_url

    def json_contains_correct_short_code(self):
        return self.code == self.short_code

    def json_contains_correct_long_url(self, long_url):
        return self.long_url == long_url
