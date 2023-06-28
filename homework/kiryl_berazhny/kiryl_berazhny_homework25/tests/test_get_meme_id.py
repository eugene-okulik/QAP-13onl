from endpoints.get_meme_id import GetMemeID


def test_get_meme_id(token):
    meme_endpoint = GetMemeID()
    meme_endpoint.get_meme_id(token)
    assert meme_endpoint.the_requested_meme_was_found
    assert meme_endpoint.meme_has_a_creator
    assert meme_endpoint.meme_has_a_description
    assert meme_endpoint.meme_has_a_tag
    assert meme_endpoint.meme_has_a_text
    assert meme_endpoint.meme_has_a_valid_url
    assert meme_endpoint.status_code_is_200


def test_get_meme_id_unauthorized_user(token='QWEFRTY'):
    un_meme_endpoint = GetMemeID()
    un_meme_endpoint.get_meme_id(token, id_meme=1)
    assert un_meme_endpoint.status_code_is_401
    assert un_meme_endpoint.correct_message_error_not_authorized
