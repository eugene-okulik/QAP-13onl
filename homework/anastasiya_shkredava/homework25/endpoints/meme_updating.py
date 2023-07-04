import requests
from endpoints.endpoint_handler import Endpoint


class MemeUpdating(Endpoint):

    updated_text = None
    updated_url = None
    updated_tags = None
    updated_info = None
    body = None

    def update_meme(self):
        self.body = {
            "id": self.get_meme_id,
            "text": "shrek meme updated",
            "url": "https://memes.com/m/3KELQpVyExX",
            "tags":
                [
                    "fun",
                    "updated shrek"
                ],
            "info": {
                "objects":
                    [
                        "updated image",
                        "updated video"
                    ]
                    }
        }
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'{self.get_token}'
        }
        response = requests.put(
            f'http://167.172.172.115:52355/meme/{self.get_meme_id}',
            json=self.body,
            headers=headers
        )
        self.status_code = response.status_code
        response_json = response.json()
        self.updated_text = response_json["text"]
        self.updated_url = response_json["url"]
        self.updated_tags = response_json["tags"]
        self.updated_info = response_json["info"]
        self.updated_text = response_json["updated_by"]

    @property
    def check_updated_url(self):
        return self.updated_url == self.body["url"]

    @property
    def check_updated_tags(self):
        return self.updated_tags == self.body["tags"]

    @property
    def check_updated_info(self):
        return self.updated_info == self.body["info"]

    @property
    def check_user_updating(self):
        return self.get_username == self.get_updated_by
