from endpoints.get_token import GetToken


def test_existing_token():
    valid_token = GetToken()
    valid_token.get_token()
    assert valid_token.response_text_contains_correct_username_for_token
    assert valid_token.status_code_is_200


def test_invalid_token():
    failed_token = GetToken()
    failed_token.invalid_token()
    assert failed_token.message_about_token_invalidity
    assert failed_token.status_code_is_404
