import pytest
from endpoints.get_token import GetToken


@pytest.fixture()
def token():
    valid_token = GetToken()
    token = valid_token.get_token()
    return token
