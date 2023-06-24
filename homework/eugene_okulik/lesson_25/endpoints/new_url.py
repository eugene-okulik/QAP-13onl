from endpoints.endpoint_handler import Endpoint
import requests


class PostNewUrl(Endpoint):
    response_json = None
    short_code = None

    def __init__(self, random_url=None):
        self.__random_url = random_url

    @property
    def random_url(self):
        return self.__random_url

    @random_url.setter
    def random_url(self, value):
        self.__random_url = value

    def post_request(self):
        if not self.__random_url:
            raise KeyError('Random URL is not set')
        body = {
            'input': self.random_url
        }
        header = {
            'Content-Type': 'application/json'
        }
        response = requests.post(
            'https://gotiny.cc/api',
            json=body,
            headers=header
        )
        self.status_code = response.status_code
        self.response_json = response.json()[0]
        self.short_code = self.response_json['code']
        return response



    @property
    def url_to_shorten_is_correct_in_the_response(self):
        return self.response_json['long'] == self.__random_url

    @property
    def short_code_is_not_empty(self):
        return len(self.short_code) > 0
