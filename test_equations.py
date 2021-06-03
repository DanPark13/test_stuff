from equations import *
import pytest

def test_always_passes():
    assert True

def test_sum():
    for first in range(5):
        for second in range(5):
            assert sum(first, second) ==  first + second

def test_diff():
    for first in range(5):
        for second in range(5):
            assert difference(first, second) ==  first - second

def test_exeception():
    with pytest.raises(SystemExit):
        exception()

class TestClassDemoInstance:
    def test_one(self):
        assert True

    def test_two(self):
        assert True