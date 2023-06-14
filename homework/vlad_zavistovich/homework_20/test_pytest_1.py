import pytest


@pytest.fixture(scope='session')
def s_session():
    print('Test start')
    yield ...
    print('Testing is finished')


@pytest.fixture(scope='function')
def s_test():
    print('Before all')
    yield ...
    print('After all')


@pytest.mark.simple
def test_plus(s_session, s_test):
    result = 1 + 1
    assert result == 2


@pytest.mark.simple
def test_minus(s_session, s_test):
    result = 2 - 1
    assert result == 1


@pytest.mark.hard
def test_mult(s_session, s_test):
    result = 2 * 2
    assert result == 4


@pytest.mark.parametrize(
    'numb',
    [2, 4, 22]
)
@pytest.mark.hard
def test_summ_par(s_session, s_test, numb):
    result = 2 + numb
    assert result == 4


@pytest.mark.hard
def test_division(s_session, s_test):
    result = 5 / 1
    assert result == 5


@pytest.mark.skip('Bug #123')
@pytest.mark.hard
def test_text(s_session, s_test):
    text_1 = 'AAAAAAA'
    assert text_1.lower() == text_1


@pytest.mark.simple
def test_text_2(s_session, s_test):
    text_2 = 'bbbbbbb'
    assert text_2.lower() == text_2


@pytest.mark.simple
def test_text_3(s_session, s_test):
    name_country = 'Argentina'
    assert len(name_country) == 9


@pytest.mark.hard
def test_text_3(s_session, s_test):
    number_r = True
    assert number_r is True


@pytest.mark.hard
def test_summ_words(s_session, s_test):
    first_part = 'United '
    second_part = 'Kingdom'
    assert first_part + second_part == 'United Kingdom'
