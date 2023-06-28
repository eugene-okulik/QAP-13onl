from endpoints.base_endpoint import BaseEndpoint
import requests
import os


class PostAuthorization(BaseEndpoint):
    response_json = None
    token = None
    username = None

    def post_username_confirmation(self, username=None):
        header = {
            'Content-type': 'application/json'
        }
        if username or username == '':
            self.username = username
            body = {
                'name': self.username
            }
        else:
            self.username = 'KirylBerazhny'
            body = {
                'name': self.username
            }
        response = requests.post(
            'http://167.172.172.115:52355/authorize',
            json=body,
            headers=header
        )
        self.status_code = response.status_code
        self.response_json = response.json()
        self.token = self.response_json['token']
        if self.username == 'KirylBerazhny':
            os_path = os.path.join(os.path.dirname(__file__), 'name_token.txt')
            with open(os_path, 'w') as name_token:
                name_token.write(self.token)
        return response

    @property
    def username_is_correct_in_the_response(self):
        return self.response_json['user'] == self.username

    @property
    def username_token_is_not_empty(self):
        return len(self.token) > 0
