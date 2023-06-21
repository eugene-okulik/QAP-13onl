import requests


def all_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    print(response[0]['title'])
    assert len(response) == 100


def one_post():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/42').json()
    print(response)
    assert response['id'] == 42


def post_a_post():
    headers = {
        'Content-type': 'application/json'
    }
    body = {
        "title": "werkherkejhrkerjh",
        "body": "lkajshdkjfahslkdjfhiquwgefkjahgsdkjasdhf",
        "userId": 1
    }
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        json=body,
        headers=headers
    )
    print(response.json())


def put_a_post():
    headers = {
        'Content-type': 'application/json'
    }
    body = {
        "title": "werkherkejhrkerjh",
        "body": "lkajshdkjfahslkdjfhiquwgefkjahgsdkjasdhf",
        "userId": 1
    }
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        json=body,
        headers=headers
    ).json()
    post_id = response['id']
    headers = {
        'Content-type': 'application/json'
    }
    body = {
        "title": "werkherkejhrkerjh-upd",
        "body": "lkajshdkjfahslkdjfhiquwgefkjahgsdkjasdhf-upd",
        "userId": 1
    }
    response = requests.put(
        f'https://jsonplaceholder.typicode.com/posts/{post_id}',
        json=body,
        headers=headers
    )
    print(response.json())


def patch_a_post():
    headers = {
        'Content-type': 'application/json'
    }
    body = {
        "title": "werkherkejhrkerjh-upd"
    }
    response = requests.patch(
        'https://jsonplaceholder.typicode.com/posts/42',
        json=body,
        headers=headers
    )
    print(response.json())


def del_a_post():
    headers = {
        'Content-type': 'application/json'
    }
    body = {
        "title": "werkherkejhrkerjh",
        "body": "lkajshdkjfahslkdjfhiquwgefkjahgsdkjasdhf",
        "userId": 1
    }
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        json=body,
        headers=headers
    ).json()
    post_id = response['id']
    response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
    print(response.status_code)
    assert response.status_code == 200
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
    assert response.status_code == 404


del_a_post()
