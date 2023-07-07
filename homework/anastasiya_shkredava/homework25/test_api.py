import pytest

from endpoints.authorization import Authorization
from endpoints.meme_creation import MemeCreation
from endpoints.meme_updating import MemeUpdating
from endpoints.meme_delition import MemeDeletion
from endpoints.get_meme import GetAll


@pytest.fixture
def delete_meme_after():
    yield None
    delete_meme = MemeDeletion()
    delete_meme.delete_meme()


@pytest.fixture
def authorization():
    user_authorization = Authorization()
    user_authorization.check_token()
    if user_authorization.status_code_is_404:
        user_authorization.user_authorization(name='Anastasiya')


def test_creating_meme(authorization, delete_meme_after):
    create_meme = MemeCreation()
    create_meme.create_meme()
    assert create_meme.status_code_is_200
    assert create_meme.check_created_text
    assert create_meme.check_created_url
    assert create_meme.check_created_tags
    assert create_meme.check_created_info
    assert create_meme.check_username


def test_updating_meme(delete_meme_after):
    create_meme = MemeCreation()
    create_meme.create_meme()
    update_meme = MemeUpdating()
    update_meme.update_meme()
    assert update_meme.status_code_is_200
    assert update_meme.check_updated_url
    assert update_meme.check_updated_tags
    assert update_meme.check_updated_info
    assert update_meme.check_user_updating


def test_deleting_meme():
    create_meme = MemeCreation()
    create_meme.create_meme()
    delete_meme = MemeDeletion()
    delete_meme.delete_meme()
    assert delete_meme.status_code_is_200
    assert delete_meme.check_response_text
    delete_meme.find_deleted_meme()
    assert delete_meme.status_code_is_404


def test_get_all_meme(delete_meme_after):
    create_meme = MemeCreation()
    create_meme.create_meme()
    get_all = GetAll()
    get_all.get_all_memes()
    get_all.find_meme_with_tag_fun()
    assert get_all.check_presence_of_fun_tag
