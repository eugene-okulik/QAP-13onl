from endpoints.base_endpoint import BaseEndpoint
import requests


class GetMemes(BaseEndpoint):
    response_json = None
    all_id_memes = None
    text = None

    def get_all_memes(self, token):
        header = {
            'Authorization': token
        }
        response = requests.get('http://167.172.172.115:52355/meme', headers=header)
        self.status_code = response.status_code
        if self.status_code == 200:
            self.response_json = response.json()
        self.text = response.text
        return response

    @property
    def one_or_more_memes_are_loaded(self):
        return len(self.response_json['data']) > 0

    def number_memes(self):
        return len(self.response_json['data'])

    @property
    def there_is_one_meme_with_tag_fun(self):
        for meme in self.response_json['data']:
            if 'fun' in meme['tags'][0]:
                return True
            else:
                return False

    @property
    def correct_message_error_not_authorized(self):
        return 'Not authorized' in self.text

    def list_all_id_memes(self, token):
        self.get_all_memes(token)
        id_memes = list()
        for meme in self.response_json['data']:
            id_memes.append(meme['id'])
        self.all_id_memes = id_memes
        return self.all_id_memes
