import requests
import os
from endpoints.endpoint_handler import Endpoint


class MemeCreation(Endpoint):

    text = None
    url = None
    tags = None
    info = None
    updated_by = None
    body = None

    def create_meme(self):
        self.body = {
            "text": "shrek meme",
            "url": "https://memes.com/m/VzBO6krdByx",
            "tags": [
                "fun",
                "shrek"
            ],
            "info": {
                "objects":
                    [
                        "image",
                        "video"
                    ]
            }
        }
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'{self.get_token}'
        }
        response = requests.post(
            'http://167.172.172.115:52355/meme',
            json=self.body,
            headers=headers
        )
        self.status_code = response.status_code
        response_json = response.json()
        self.text = response_json["text"]
        self.url = response_json["url"]
        self.tags = response_json["tags"]
        self.info = response_json["info"]
        self.updated_by = response_json["updated_by"]
        path = os.path.dirname(__file__)
        sys_path = os.path.join(path, 'memes.txt')
        with open(sys_path, 'w') as save_meme:
            save_meme.write(response.text)

    @property
    def check_created_text(self):
        return self.text == self.body["text"]

    @property
    def check_created_url(self):
        return self.url == self.body["url"]

    @property
    def check_created_tags(self):
        return self.tags == self.body["tags"]

    @property
    def check_created_info(self):
        return self.info == self.body["info"]

    @property
    def check_username(self):
        return self.get_username == self.updated_by
