from endpoints.post_new_meme import PostNewMeme


def test_post_new_meme(token):
    new_meme = PostNewMeme()
    new_meme.post_new_meme(token)
    assert new_meme.status_code_is_200
    assert new_meme.tags_check
    assert new_meme.text_check
    assert new_meme.url_check
    assert new_meme.username_check
    assert new_meme.meme_added_and_id_is_in_the_list(token)


def test_post_new_meme_unauthorized_user(token='QWEFRTY'):
    new_meme = PostNewMeme()
    new_meme.post_new_meme(token)
    assert new_meme.status_code_is_401
    assert new_meme.correct_message_error_not_authorized


# def test_post_new_meme_with_an_over_field(token):  # мем добавляется, лишнее поле в описании не отображается <200>
#     new_meme = PostNewMeme()                       # чисто в теории я думаю должна быть ошибка 500
#     new_meme.post_new_meme(token, field='over')
#     assert new_meme.status_code_is_500
#     assert new_meme.correct_message_internal_server_error


def test_post_new_meme_with_an_miss_field(token):
    new_meme = PostNewMeme()
    new_meme.post_new_meme(token, field='miss')
    assert new_meme.status_code_is_500
    assert new_meme.correct_message_internal_server_error


def test_post_new_meme_with_an_incorrectly_filled_in_parameter(token):
    new_meme = PostNewMeme()
    new_meme.post_new_meme(token, field='unfilled')
    assert new_meme.status_code_is_400
    assert new_meme.correct_message_error_bad_request
