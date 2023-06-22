import pytest


@pytest.fixture(scope="module", autouse=True)
def setup_module():
    print('before all')
    yield
    print('after all')


@pytest.fixture(autouse=True)
def setup_function():
    print('before each test')
    yield
    print('after each test')


@pytest.mark.simple
@pytest.mark.parametrize("a, b, expected_result", [(2, 2, 4), (3, 5, 8), (0, 0, 0)])
def test_add(a, b, expected_result):
    result = a + b
    assert result == expected_result


@pytest.mark.simple
@pytest.mark.skip("Skipping subtraction test")
def test_subtr():
    assert 10 - 5 == 5


@pytest.mark.simple
def test_multi():
    assert 3 * 4 == 12


@pytest.mark.simple
def test_div():
    assert 10 / 2 == 5


@pytest.mark.hard
def test_expo():
    assert 2 ** 3 == 8


@pytest.mark.hard
def test_floor_div():
    assert 10 // 3 == 3


@pytest.mark.hard
def test_modul():
    assert 10 % 3 == 1


@pytest.mark.simple
def test_greater_than():
    assert 5 > 3


@pytest.mark.simple
def test_less_than():
    assert 2 < 7


@pytest.mark.simple
def test_equality():
    assert 7 == 7
