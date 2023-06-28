from endpoints.post_authorization_user import PostAuthorization


def test_authorization():
    username_endpoint = PostAuthorization()
    username_endpoint.post_username_confirmation()
    assert username_endpoint.status_code_is_200
    assert username_endpoint.username_is_correct_in_the_response
    assert username_endpoint.username_token_is_not_empty


def test_authorization_with_an_empty_field():
    username_endpoint = PostAuthorization()
    username_endpoint.post_username_confirmation(username='')
    assert username_endpoint.status_code_is_200
    assert username_endpoint.username_is_correct_in_the_response
    assert username_endpoint.username_token_is_not_empty


def test_authorization_with_special_signs():
    username_endpoint = PostAuthorization()
    username_endpoint.post_username_confirmation(username='!"№%:, .;()][`')
    assert username_endpoint.status_code_is_200
    assert username_endpoint.username_is_correct_in_the_response
    assert username_endpoint.username_token_is_not_empty
