import pytest
import random
import string

from endpoints.new_url import PostNewUrl


@pytest.fixture(scope='function')
def random_url():
    letters = string.ascii_lowercase
    name_str = ''.join(random.choice(letters) for i in range(7))
    domain_str = ''.join(random.choice(letters) for i in range(2))
    return f'https://{name_str}.{domain_str}'


@pytest.fixture()
def create_short_url(random_url):
    new_url_endp = PostNewUrl(random_url)
    new_url_endp.post_request()
    short_code = new_url_endp.short_code
    return short_code

