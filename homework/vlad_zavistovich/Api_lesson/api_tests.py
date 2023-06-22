import requests


def all_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    print(response[0]['title'])

def one_post():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/42').json()
    print(response)

def post_a_post():
    headers = {
        'Content-type': 'application/json; charset=UTF-8',
    }
    body = {
        "title": "12123",
        "body": "bar",
        "userId": 1
    }
    response = requests.post('https://jsonplaceholder.typicode.com/posts', json=body, headers=headers)
    print(response.json())

def put_a_post():
    headers = {
        'Content-type': 'application/json; charset=UTF-8',
    }
    body = {
        "title": "1212399",
        "body": "barrr",
        "userId": 1
    }
    response = requests.put('https://jsonplaceholder.typicode.com/posts/42', json=body, headers=headers)
    print(response.json())

def patch_a_post():
    headers = {
        'Content-type': 'application/json; charset=UTF-8',
    }
    body = {
        "title": "989898",
        "userId": 1
    }
    response = requests.patch('https://jsonplaceholder.typicode.com/posts/42', json=body, headers=headers)
    print(response.json())

def del_a_post():
    response = requests.delete('https://jsonplaceholder.typicode.com/posts/42')
    print(response.status_code)

del_a_post()
