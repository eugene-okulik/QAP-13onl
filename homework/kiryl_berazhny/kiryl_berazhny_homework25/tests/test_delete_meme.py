from endpoints.delete_meme import DeleteMeme


def test_delete_my_new_meme_(token):
    del_meme = DeleteMeme()
    del_meme.delete_meme(token)
    assert del_meme.correct_message_about_deleting_a_meme
    assert del_meme.status_code_is_200
    assert del_meme.meme_id_removed_from_memes_list


def test_delete_someone_else_new_meme_(token):  # здесь пока не придумал как создать/найти мем от одного пользователя
    del_meme = DeleteMeme()                     # и удалить от другого
    del_meme.delete_meme(token, 28)
    assert del_meme.correct_message_error_meme_owner
    assert del_meme.status_code_is_400


def test_delete_new_meme_unauthorized_user(token='QWEFRTY'):
    del_meme = DeleteMeme()
    del_meme.delete_meme(token, manual_id=1)
    assert del_meme.correct_message_error_not_authorized
    assert del_meme.status_code_is_401


def test_delete_meme_invalid_id(token):
    del_meme = DeleteMeme()
    del_meme.delete_meme(token, manual_id=-1)
    assert del_meme.status_code_is_404
    assert del_meme.error_message_404_not_found
