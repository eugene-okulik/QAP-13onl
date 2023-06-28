from endpoints.base_endpoint import BaseEndpoint
from endpoints.get_memes import GetMemes
import random
import requests


class GetMemeID(BaseEndpoint):
    response_json = None
    id_meme = None
    text = None

    def random_id_meme(self, token):
        all_id = GetMemes().list_all_id_memes(token)
        id_meme = all_id[random.randint(0, len(all_id) - 1)]
        self.id_meme = id_meme
        return self.id_meme

    def get_meme_id(self, token, id_meme=None):
        header = {
            'Authorization': token
        }
        if id_meme:
            response = requests.get(f'http://167.172.172.115:52355/meme/{id_meme}', headers=header)
            self.id_meme = id_meme
        else:
            id_meme = self.random_id_meme(token)
            response = requests.get(f'http://167.172.172.115:52355/meme/{id_meme}', headers=header)
        self.status_code = response.status_code
        if self.status_code == 200:
            self.response_json = response.json()
        self.text = response.text
        return response

    @property
    def the_requested_meme_was_found(self):
        return self.response_json['id'] == self.id_meme

    @property
    def meme_has_a_description(self):
        return len(self.response_json['info']) > 0

    @property
    def meme_has_a_tag(self):
        return len(self.response_json['tags']) > 0

    @property
    def meme_has_a_text(self):
        return len(self.response_json['text']) > 0

    @property
    def meme_has_a_creator(self):
        return len(self.response_json['updated_by']) > 0

    @property
    def meme_has_a_valid_url(self):
        url = requests.get(self.response_json['url'])
        return url.status_code == 200

    @property
    def correct_message_error_not_authorized(self):
        return 'Not authorized' in self.text
