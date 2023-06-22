import pytest


@pytest.fixture()
def say_each_test():
    print('Printed text before each test')
    yield None
    print('Printed text after each test')


@pytest.fixture(scope='session')
def say_all_tests():
    print('Before all tests')
    yield None
    print('After all tests')


@pytest.mark.hard
def test1(say_all_tests, say_each_test):
    a = 1 + 3
    assert a == 4


@pytest.mark.hard
def test2(say_each_test):
    a = 3 + 3
    assert a == 6


@pytest.mark.hard
def test3():
    a = 4 + 3
    assert a == 7


@pytest.mark.hard
def test4():
    a = 7 + 3
    assert a == 10


@pytest.mark.hard
def test5():
    a = 2 + 3
    assert a == 5


@pytest.mark.hard
def test6():
    a = 8 + 3
    assert a == 11


@pytest.mark.hard
def test7():
    a = 2 - 3
    assert a == -1


@pytest.mark.hard
def test8():
    a = 15 + 3
    assert a == 18


@pytest.mark.skip(reason='bug#1337')
def test9():
    a = 11 + 3
    assert a == 14


@pytest.mark.parametrize('numb', [0, 1, 2, 3])
@pytest.mark.hard
def test10(numb):
    a = 19 + numb
    assert a == 22
