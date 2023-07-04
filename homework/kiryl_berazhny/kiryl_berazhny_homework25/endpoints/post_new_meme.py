from endpoints.base_endpoint import BaseEndpoint
from endpoints.get_memes import GetMemes
import requests


class PostNewMeme(BaseEndpoint):
    response_json = None
    text = None

    def post_new_meme(self, token, field=None):
        header = {
            'Content-type': 'application/json',
            'Authorization': token
        }
        if field == 'over':
            body = {
                'id': '123',
                'text': 'А монитор у него есть?',
                'url':
                    'https://encrypted-tbn0.gstatic.com/images?q=tbn:'
                    'ANd9GcRkGYpXAbxZKaLb7y1p9LXaz2Cbe-mu71DTjA&usqp=CAU',
                'tags': ["fun", "TV"],
                'info': {
                    "colors": ["green", "black", "white"],
                    "objects": ["picture", "text"]
                }
            }
        elif field == 'miss':
            body = {
                'text': 'А монитор у него есть?',
                'tags': ["fun", "TV"],
                'info': {
                    "colors": ["green", "black", "white"],
                    "objects": ["picture", "text"]
                }
            }
        elif field == 'unfilled':
            body = {
                'text': 'А монитор у него есть?',
                'url':
                    'https://encrypted-tbn0.gstatic.com/'
                    'images?q=tbn:ANd9GcRkGYpXAbxZKaLb7y1p9LXaz2Cbe-mu71DTjA&usqp=CAU',
                'tags': ["fun", "TV"],
                'info': ''
            }
        else:
            body = {
                'text': 'А монитор у него есть?',
                'url':
                    'https://encrypted-tbn0.gstatic.com/'
                    'images?q=tbn:ANd9GcRkGYpXAbxZKaLb7y1p9LXaz2Cbe-mu71DTjA&usqp=CAU',
                'tags': ["fun", "TV"],
                'info': {
                    "colors": ["green", "black", "white"],
                    "objects": ["picture", "text"]
                }
            }
        response = requests.post(
            'http://167.172.172.115:52355/meme',
            json=body,
            headers=header
        )
        self.status_code = response.status_code
        if self.status_code == 200:
            self.response_json = response.json()
        self.text = response.text
        return response

    @property
    def username_check(self):
        return self.response_json['updated_by'] == 'KirylBerazhny'

    @property
    def text_check(self):
        return self.response_json['text'] == 'А монитор у него есть?'

    @property
    def url_check(self):
        return self.response_json['url'] == (
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRkGYpXAbxZKaLb7y1p9LXaz2Cbe-mu71DTjA&usqp=CAU')

    @property
    def tags_check(self):
        return self.response_json['tags'] == ["fun", "TV"]

    @property
    def info_check(self):
        return self.response_json['info'] == {"colors": ["green", "black", "white"], "objects": ["picture", "text"]}

    @property
    def correct_message_error_not_authorized(self):
        return 'Not authorized' in self.text

    @property
    def correct_message_internal_server_error(self):
        return 'Internal Server Error' in self.text

    @property
    def correct_message_error_bad_request(self):
        return '400 Bad Request' in self.text

    def meme_added_and_id_is_in_the_list(self, token):
        list_id = GetMemes().list_all_id_memes(token)
        return self.response_json['id'] in list_id
