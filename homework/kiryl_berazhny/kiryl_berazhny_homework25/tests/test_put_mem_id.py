from endpoints.put_meme_id import PutMemeId


def test_put_my_meme(token):
    put_new_meme = PutMemeId()
    put_new_meme.put_meme(token)
    assert put_new_meme.status_code_is_200
    assert put_new_meme.tags_check
    assert put_new_meme.text_check
    assert put_new_meme.url_check
    assert put_new_meme.username_check
    assert put_new_meme.id_check


def test_put_someone_else_meme(token):
    put_new_meme = PutMemeId()
    put_new_meme.put_meme(token, manual_id=28)
    assert put_new_meme.status_code_is_400
    assert put_new_meme.correct_message_error_meme_owner


def test_put_meme_with_invalid_id(token):
    put_new_meme = PutMemeId()
    put_new_meme.put_meme(token, manual_id=-1)
    assert put_new_meme.status_code_is_404
    assert put_new_meme.error_message_404_not_found


def test_put_meme_unauthorized_user(token):
    put_new_meme = PutMemeId()
    id_meme = put_new_meme.id_new_post_meme(token)
    put_new_meme.put_meme(token='QWEFRTY', manual_id=id_meme)
    assert put_new_meme.correct_message_error_not_authorized
    assert put_new_meme.status_code_is_401


# def test_put_meme_with_an_over_field(token):  # мем изменяется, лишнее поле в описании не отображается, <200>
#     put_new_meme = PutMemeId()                # чисто в теории я думаю должна быть ошибка 500
#     put_new_meme.put_meme(token, field='over')
#     assert put_new_meme.status_code_is_500
#     assert put_new_meme.correct_message_internal_server_error


def test_put_meme_with_an_miss_field(token):
    put_new_meme = PutMemeId()
    put_new_meme.put_meme(token, field='miss')
    assert put_new_meme.status_code_is_500
    assert put_new_meme.correct_message_internal_server_error


def test_put_meme_with_an_incorrectly_filled_in_parameter(token):
    put_new_meme = PutMemeId()
    put_new_meme.put_meme(token, field='unfilled')
    assert put_new_meme.status_code_is_400
    assert put_new_meme.correct_message_error_bad_request
