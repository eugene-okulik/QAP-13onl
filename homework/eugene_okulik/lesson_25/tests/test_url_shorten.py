from endpoints.new_url import PostNewUrl


def test_random_shortener(random_url):
    new_url_endpoint = PostNewUrl()
    new_url_endpoint.random_url = random_url
    new_url_endpoint.post_request()
    assert new_url_endpoint.status_code_is_200
    assert new_url_endpoint.url_to_shorten_is_correct_in_the_response
    assert new_url_endpoint.short_code_is_not_empty
