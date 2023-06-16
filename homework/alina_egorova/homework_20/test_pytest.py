import pytest
from datetime import datetime


@pytest.fixture(scope='session')
def action():
    print('before all')
    yield None
    print('after all')


@pytest.fixture()
def every():
    print('before each test')
    yield None
    print(' after each test')


def test_one(action, every):
    summ = 5 + 7
    assert summ == 12


@pytest.mark.skipif(datetime.now().weekday() == 4, reason='Not working in Friday')
def test_two(every):
    subtraction = 10 - 3
    assert subtraction == 7


@pytest.mark.simple
def test_three(every):
    multiplication = 5 * 5
    assert multiplication == 25


@pytest.mark.hard
@pytest.mark.parametrize(
    'num',
    [0, 2, 5, 8, 3, 4, 7]
)
def test_four(every, num):
    subtraction2 = num - 3
    assert subtraction2 == 1


def test_five(every):
    division = 15 / 3
    assert division == 5


@pytest.mark.skip('Bug #666')
def test_six(every):
    multiplication2 = 4 * 5
    assert multiplication2 == 20


@pytest.mark.simple
def test_seven(every):
    division2 = 20 / 5
    assert division2 == 4


@pytest.mark.parametrize(
    'num1',
    [0, 2, 5, 8, 3]
)
def test_eight(every, num1):
    summ2 = num1 + 7
    assert summ2 == 15


@pytest.mark.hard
@pytest.mark.parametrize(
    'num2',
    [2, 3, 4, 5, 6]
)
def test_nine(every, num2):
    degree = 5 ** num2
    assert degree == 625


@pytest.mark.hard
def test_ten(every):
    degree2 = 3 ** 5
    assert degree2 == 243
