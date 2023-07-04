from endpoints.get_memes import GetMemes


def test_get_all_memes(token):
    memes_endpoint = GetMemes()
    memes_endpoint.get_all_memes(token)
    assert memes_endpoint.status_code_is_200
    assert memes_endpoint.one_or_more_memes_are_loaded
    assert memes_endpoint.there_is_one_meme_with_tag_fun


def test_get_all_memes_unauthorized_user(token='QWEFRTY'):
    memes_endpoint = GetMemes()
    memes_endpoint.get_all_memes(token)
    assert memes_endpoint.status_code_is_401
    assert memes_endpoint.correct_message_error_not_authorized
