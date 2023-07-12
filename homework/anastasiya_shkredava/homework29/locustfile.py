import os
from locust import task, HttpUser
from dotenv import load_dotenv


class QuikStartUser(HttpUser):
    load_dotenv()
    long_url = os.getenv('url')
    code = None

    def on_start(self):
        response = self.client.post(
            '/api',
            json={"input": f"{self.long_url}"}
        )
        self.code = response.json()[0]["code"]

    @task
    def get_long_url(self):
        self.client.get(
            f'/api/{self.code}'
        )

    @task
    def get_site(self):
        self.client.get(
            f'/{self.code}'
        )
