import requests
import os
from endpoints.endpoint_handler import Endpoint


class Authorization(Endpoint):
    sent_name = None
    user_name = None
    token = None

    def check_token(self):
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.get(
            f'http://167.172.172.115:52355/authorize/{self.get_token}',
            headers=headers
        )
        self.status_code = response.status_code
        return self.status_code

    def user_authorization(self, name):
        body = {
            "name": f"{name}"
        }
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(
            'http://167.172.172.115:52355/authorize',
            json=body,
            headers=headers
        )
        response_json = response.json()
        self.status_code = response.status_code
        self.token = response_json['token']
        self.user_name = response_json['user']
        path = os.path.dirname(__file__)
        sys_path = os.path.join(path, 'token.txt')
        with open(sys_path, 'w') as save_token:
            save_token.write(f'{self.user_name} {self.token}')
