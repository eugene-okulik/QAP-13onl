import random
from locust import task, HttpUser


class QuikStartUser(HttpUser):
    token = ''

    def on_start(self):
        response = self.client.post(
            '/authorize',
            json={'name': 'Vasia'}
        )
        self.token = response.json()['token']

    @task
    def get_memes(self):
        self.client.get(
            '/meme',
            headers={'Authorization': self.token}
        )

    @task
    def get_meme(self):
        ids = [38, 717, 246, 120]
        self.client.get(
            f'/meme/{random.choice(ids)}',
            headers={'Authorization': self.token}
        )
