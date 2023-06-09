import pytest


@pytest.fixture(scope='session')
def session_action():
    print('before all')
    yield None
    print('after all')


@pytest.fixture()
def test_action():
    print('test started')
    yield None
    print('test ended')


@pytest.mark.simple
def test_one(session_action, test_action):
    summ = 3 + 2
    assert summ == 8


@pytest.mark.hard
def test_two(test_action):
    div = 4 / 2
    assert div != 4


@pytest.mark.simple
def test_three(test_action):
    mult = 8 * 4
    assert mult > 24


@pytest.mark.simple
def test_four(test_action):
    a = ''
    assert bool(a)


@pytest.mark.skip('Bug #456')
def test_five(test_action):
    a = 'adf32'
    assert a.isdigit()


@pytest.mark.parametrize(
    'a',
    ['12345', '123456', '1234567']
)
@pytest.mark.simple
def test_six(test_action, a):
    password = len(a)
    assert password < 6


@pytest.mark.parametrize(
    "input_data, expected_result",
    [('11 * 11', 121), ("5 / 4", 1), ("6 + 9", 15)]
)
@pytest.mark.hard
def test_seven(test_action, input_data, expected_result):
    assert eval(input_data) == expected_result


@pytest.mark.parametrize(
    "side1, side2",
    [(2, 3), (5, 5), (6, 8)]
)
def test_eight(test_action, side1, side2):
    assert side1 == side2


def test_nine(test_action):
    numb = 7
    assert numb >= 7


def test_ten(test_action):
    text = "Hello, World"
    assert text.lower()
