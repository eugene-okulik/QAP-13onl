import requests
from endpoints.endpoint_handler import Endpoint


class MemeDeletion(Endpoint):

    response_text = None

    def delete_meme(self):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'{self.get_token}'
        }
        response = requests.delete(
            f'http://167.172.172.115:52355/meme/{self.get_meme_id}',
            headers=headers
        )
        self.response_text = response.text
        self.status_code = response.status_code

    @property
    def check_response_text(self):
        text = f'Meme with id {self.get_meme_id} successfully deleted'
        return self.response_text == text

    def find_deleted_meme(self):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'{self.get_token}'
        }
        response = requests.get(
            f'http://167.172.172.115:52355/meme/{self.get_meme_id}',
            headers=headers
        )
        self.status_code = response.status_code
        return self.status_code
