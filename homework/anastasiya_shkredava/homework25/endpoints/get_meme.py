import requests
from endpoints.endpoint_handler import Endpoint


class GetAll(Endpoint):

    response_json = None
    memes_with_fun_tag = []

    def get_all_memes(self):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'{self.get_token}'
        }
        response = requests.get(
            'http://167.172.172.115:52355/meme',
            headers=headers
        )
        self.status_code = response.status_code
        self.response_json = response.json()

    def find_meme_with_tag_fun(self):
        for meme in self.response_json['data']:
            for tag in meme['tags']:
                if tag == 'fun':
                    self.memes_with_fun_tag.append(meme)
        return self.memes_with_fun_tag

    @property
    def check_presence_of_fun_tag(self):
        if len(self.memes_with_fun_tag) > 0:
            return True
