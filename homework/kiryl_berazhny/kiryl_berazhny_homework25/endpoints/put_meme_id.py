from endpoints.base_endpoint import BaseEndpoint
from endpoints.post_new_meme import PostNewMeme
import requests


class PutMemeId(BaseEndpoint):
    response_json = None
    id_meme = None
    text = None

    def id_new_post_meme(self, token):
        post_meme = PostNewMeme()
        new_meme = post_meme.post_new_meme(token).json()
        self.id_meme = new_meme['id']
        return self.id_meme

    def put_meme(self, token, manual_id=None, field=None):
        if manual_id or manual_id == 0:
            meme_id = manual_id
        else:
            meme_id = self.id_new_post_meme(token)
        headers = {
            'Content-type': 'application/json',
            'Authorization': token
        }
        if field == 'over':
            body = {
                'id': meme_id,
                'text': 'Когда одного недостаточно',
                'url':
                    'https://memepedia.ru/wp-content/uploads/2017/12/tl9sa0.jpg',
                'tags': ["fun", "startrack", "facepalm"],
                'info': {
                    "colors": ["red", "black", "white", "blue"],
                    "objects": ["picture", "text"]
                },
                'over_field': 'overt_field'
            }
        elif field == 'miss':
            body = {
                'id': meme_id,
                'text': 'Когда одного недостаточно',
                'tags': ["fun", "startrack", "facepalm"],
                'info': {
                    "colors": ["red", "black", "white", "blue"],
                    "objects": ["picture", "text"]
                }
            }
        elif field == 'unfilled':
            body = {
                'id': meme_id,
                'text': 'Когда одного недостаточно',
                'url':
                    'https://memepedia.ru/wp-content/uploads/2017/12/tl9sa0.jpg',
                'tags': ["fun", "startrack", "facepalm"],
                'info': 'fail_field'
            }
        else:
            body = {
                'id': meme_id,
                'text': 'Когда одного недостаточно',
                'url':
                    'https://memepedia.ru/wp-content/uploads/2017/12/tl9sa0.jpg',
                'tags': ["fun", "startrack", "facepalm"],
                'info': {
                    "colors": ["red", "black", "white", "blue"],
                    "objects": ["picture", "text"]
                }
            }
        response = requests.put(
            f'http://167.172.172.115:52355/meme/{meme_id}',
            json=body,
            headers=headers
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
        return self.response_json['text'] == 'Когда одного недостаточно'

    @property
    def url_check(self):
        return self.response_json['url'] == 'https://memepedia.ru/wp-content/uploads/2017/12/tl9sa0.jpg'

    @property
    def tags_check(self):
        return self.response_json['tags'] == ["fun", "startrack", "facepalm"]

    @property
    def info_check(self):
        return self.response_json['info'] == {
            "colors": ["red", "black", "white", "blue"],
            "objects": ["picture", "text"]
        }

    @property
    def id_check(self):
        return self.response_json['id'] == self.id_meme

    @property
    def correct_message_error_not_authorized(self):
        return 'Not authorized' in self.text

    @property
    def error_message_404_not_found(self):
        return '404 Not Found' in self.text

    @property
    def correct_message_error_bad_request(self):
        return '400 Bad Request' in self.text

    @property
    def correct_message_internal_server_error(self):
        return 'Internal Server Error' in self.text

    @property
    def correct_message_error_meme_owner(self):
        return 'You are not the meme owner' in self.text
