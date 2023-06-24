import requests

from endpoints.get_url_info import GetUrlInfo


def test_existing_url(random_url, create_short_url):
    short_code = create_short_url
    url_info = GetUrlInfo(short_code)
    assert url_info.status_code_is_200
    assert url_info.response_text_contains_correct_url(long_url=random_url)


def test_json_format(random_url, create_short_url):
    short_code = create_short_url
    url_info = GetUrlInfo(short_code, json_format=True)
    assert url_info.status_code_is_200
    assert url_info.json_contains_correct_short_code()
    assert url_info.json_contains_correct_long_url(random_url)
