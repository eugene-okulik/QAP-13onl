import pytest


@pytest.fixture(scope="session", autouse=True)
def before_all():
    print("Before all")


@pytest.fixture(autouse=True)
def before_each():
    print("Before each")
    yield
    print("After each")


def test_add():
    assert 2 + 2 == 4


def test_take_away():
    assert 5 - 3 == 2


def test_multiply():
    assert 6 * 7 == 42


@pytest.mark.parametrize("a, b, c", [(2, 3, 5), (4, 6, 10)])
def test_parametrized_addition(a, b, c):
    assert a + b == c


@pytest.mark.skip(reason="Not implemented yet")
def test_skipped_test():
    assert False


@pytest.mark.simple
def test_simple():
    assert True


@pytest.mark.hard
def test_hard():
    assert True


def pytest_session_finish(session, exit_status):
    print("After all")
