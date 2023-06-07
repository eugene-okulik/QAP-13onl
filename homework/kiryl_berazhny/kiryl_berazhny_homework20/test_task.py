import pytest


@pytest.fixture(scope='session')
def sf_session():
    print('Start testing')
    yield ...
    print('Finish testing')


@pytest.fixture(scope='function')
def sf_test():
    print('Before')
    yield ...
    print('After')


@pytest.mark.simple
def test_plus(sf_session, sf_test):
    result = 5 + 5
    assert result == 10


@pytest.mark.hard
def test_minus(sf_session, sf_test):
    result = 10 - 5
    assert result == 5


@pytest.mark.simple
def test_div(sf_session, sf_test):
    result = 50 / 2
    assert result == 25


@pytest.mark.parametrize(
    'numb',
    [2, 3, 4]
)
@pytest.mark.hard
def test_mult(sf_session, sf_test, numb):
    result = 33 * numb
    assert result == 99


@pytest.mark.simple
def test_len_text(sf_session, sf_test):
    text = 'Hello World'
    assert len(text) == 11


@pytest.mark.hard
def test_low_text(sf_session, sf_test):
    text = 'KIRYL'
    text2 = 'kiryl'
    assert text.lower() == text2


@pytest.mark.simple
def test_high_text(sf_session, sf_test):
    text = 'berazhny'
    text2 = 'BERAZHNY'
    assert text.upper() == text2


@pytest.mark.hard
def test_digit(sf_session, sf_test):
    numb = '09051993'
    assert numb.isdigit() is True


@pytest.mark.simple
def test_alpha_bet(sf_session, sf_test):
    text = 'kirylberag'
    assert text.isalpha() is True


@pytest.mark.hard
@pytest.mark.skip('Bug #616')
def test_philosophy(sf_session, sf_test):
    text = 'прекрасное'
    assert text == 'прекрасное'
