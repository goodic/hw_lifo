import pytest
from main import LiFo

test_stack1 = LiFo()
test_stack2 = LiFo()

element1 = 'test1'
element2 = '2'


def test_size():
    assert test_stack1.size() == 0
    assert test_stack2.size() == 0


def test_push():
    assert test_stack1.push(element1) is None
    assert test_stack1.size() == 1
    assert test_stack2.size() == 0
    assert test_stack1.push(element2) is None

    assert test_stack1.size() == 2
    assert test_stack2.size() == 0


def test_peek():
    assert test_stack1.peek() == element2
    assert test_stack2.peek() is None


def test_pop():
    assert test_stack1.pop() == element1
    assert test_stack2.pop() is None