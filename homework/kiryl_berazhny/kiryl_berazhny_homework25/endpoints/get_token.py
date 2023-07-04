from endpoints.base_endpoint import BaseEndpoint
from endpoints.post_authorization_user import PostAuthorization
import requests
import os


class GetToken(BaseEndpoint):
    text = None
    token = None

    def get_token(self):
        os_path = os.path.join(os.path.dirname(__file__), 'name_token.txt')
        with open(os_path, 'r') as name_token:
            token = name_token.readline()
        response = requests.get(f'http://167.172.172.115:52355/authorize/{token}')
        self.text = response.text
        self.status_code = response.status_code
        self.token = token
        if self.status_code != 200:
            creating_a_new_token = PostAuthorization()
            creating_a_new_token.post_username_confirmation()
            self.get_token()
        return token

    def invalid_token(self):
        response = requests.get('http://167.172.172.115:52355/authorize/XXXXXXXXXXX')
        self.text = response.text
        self.status_code = response.status_code

    @property
    def response_text_contains_correct_username_for_token(self):
        return self.text == 'Token is alive. Username is KirylBerazhny'

    @property
    def message_about_token_invalidity(self):
        return 'Token not found' in self.text
