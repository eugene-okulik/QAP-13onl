import pytest


@pytest.fixture(scope='session')
def before_and_after_all():
    print("Before all")
    yield
    print("After all")


@pytest.fixture(scope='function')
def before_and_after_test():
    print("Start test")
    yield
    print("End test")


@pytest.mark.skip('Bug #666')
@pytest.mark.simple
def test_equal(before_and_after_all, before_and_after_test):
    assert 2 + 2 == 4


@pytest.mark.simple
def test_minus(before_and_after_all, before_and_after_test):
    assert 4 - 2 == 2


@pytest.mark.simple
def test_divide(before_and_after_all, before_and_after_test):
    assert 8 / 2 == 4


@pytest.mark.simple
def test_length(before_and_after_all, before_and_after_test):
    my_list = [1, 2, 3]
    assert len(my_list) == 3


@pytest.mark.simple
def test_contains_element(before_and_after_all, before_and_after_test):
    my_list = [1, 2, 3]
    assert 2 in my_list


@pytest.mark.hard
def test_equal_strings(before_and_after_all, before_and_after_test):
    assert "hello" == "hello"


@pytest.mark.hard
def test_not_equal_strings(before_and_after_all, before_and_after_test):
    assert "hello" != "world"


@pytest.mark.hard
def test_is_true(before_and_after_all, before_and_after_test):
    assert 3 > 2


@pytest.mark.hard
def test_is_true_2(before_and_after_all, before_and_after_test):
    assert 1 < 2


@pytest.mark.hard
def test_variable_type(before_and_after_all, before_and_after_test):
    my_var = 10
    assert isinstance(my_var, int)


@pytest.mark.parametrize("num, expected", [(1, 2), (2, 4)])
def test_double(num, expected):
    assert num * 2 == expected
