import pytest


@pytest.fixture(scope='session')  # before and after testing
def test_ba():
    print('\nbefore all')
    yield None
    print('\nafter all')


@pytest.fixture(scope='function')  # before and after every testing
def test_ba_every():
    print('\nHello!')
    yield None
    print('\nBye!')


@pytest.mark.parametrize(
    'numb',
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
)
@pytest.mark.simple
def test_one(numb, test_ba, test_ba_every):
    summ = numb + 2
    assert 4 <= summ <= 9


@pytest.mark.skip('So hard!')
@pytest.mark.hard
def test_two(test_ba_every):
    summ = 2 + 3
    assert summ == 5


@pytest.mark.parametrize(
    ('str1', 'str2'),
    [('dkls', 'kew'), ('p', 'q'), ('wodk;w', 'owijd'), ('1234', '0987')]
)
@pytest.mark.simple
def test_three(str1, str2, test_ba_every):
    assert len(str1) == len(str2)


@pytest.mark.hard
def test_four(test_ba_every):
    summ = 4 + 5
    assert summ == 9


@pytest.mark.simple
def test_five(test_ba_every):
    assert 'semaphore'.capitalize() == 'Semaphore'


@pytest.mark.hard
def test_six(test_ba_every):
    assert 'abcd2'.isalpha()


@pytest.mark.simple
def test_seven(test_ba_every):
    assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]


@pytest.mark.hard
def test_eight(test_ba_every):
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    assert a * b >= 5


@pytest.mark.simple
def test_nine(test_ba_every):
    string = 'hello world!'
    assert string.title() == 'Hello world!'


@pytest.mark.hard
def test_ten(test_ba_every):
    a = 5
    assert int(a)
