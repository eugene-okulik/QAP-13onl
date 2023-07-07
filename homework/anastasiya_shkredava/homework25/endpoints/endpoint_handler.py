import os
import json


class Endpoint:
    status_code = None

    @property
    def status_code_is_200(self):
        return self.status_code == 200

    @property
    def status_code_is_404(self):
        return self.status_code == 404

    @property
    def get_token(self):
        path = os.path.dirname(__file__)
        sys_path = os.path.join(path, 'token.txt')
        with open(sys_path, 'r') as save_token:
            data = save_token.read().split()
            token = data[1]
        return token

    @property
    def get_username(self):
        path = os.path.dirname(__file__)
        sys_path = os.path.join(path, 'token.txt')
        with open(sys_path, 'r') as save_token:
            data = save_token.read().split()
            username = data[0]
        return username

    @property
    def get_meme_id(self):
        path = os.path.dirname(__file__)
        sys_path = os.path.join(path, 'memes.txt')
        with open(sys_path, 'r') as save_meme:
            data = json.load(save_meme)
            meme_id = data['id']
        return meme_id

    @property
    def get_updated_by(self):
        path = os.path.dirname(__file__)
        sys_path = os.path.join(path, 'memes.txt')
        with open(sys_path, 'r') as save_meme:
            data = json.load(save_meme)
            username = data['updated_by']
        return username
