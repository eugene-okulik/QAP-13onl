from endpoints.base_endpoint import BaseEndpoint
from endpoints.get_memes import GetMemes
from endpoints.post_new_meme import PostNewMeme
import requests


class DeleteMeme(BaseEndpoint):
    response_json = None
    id_meme = None
    all_id_memes = None
    text = None

    def delete_meme(self, token, manual_id=None):
        if manual_id or manual_id == 0:
            id_meme = manual_id
        else:
            post_meme = PostNewMeme()
            new_meme = post_meme.post_new_meme(token).json()
            id_meme = new_meme['id']
        header = {
            'Content-type': 'application/json',
            'Authorization': token
        }
        response = requests.delete(f'http://167.172.172.115:52355/meme/{id_meme}', headers=header)
        self.status_code = response.status_code
        if self.status_code == 200:
            self.all_id_memes = GetMemes().list_all_id_memes(token)
        self.response_json = response
        self.id_meme = id_meme
        self.text = response.text
        return response

    @property
    def correct_message_about_deleting_a_meme(self):
        return self.response_json.text == f'Meme with id {self.id_meme} successfully deleted'

    @property
    def meme_id_removed_from_memes_list(self):
        return self.id_meme not in self.all_id_memes

    @property
    def correct_message_error_not_authorized(self):
        return 'Not authorized' in self.text

    @property
    def error_message_404_not_found(self):
        return '404 Not Found' in self.text

    @property
    def correct_message_error_meme_owner(self):
        return 'You are not the meme owner' in self.text
