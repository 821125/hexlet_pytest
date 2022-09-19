import pytest

def test_stack():
    stack = []
    #add two elements to stack and then extract it
    stack.append('one')
    stack.append('two')

    assert stack.pop() == 'two'
    assert stack.pop() == 'one'


def test_emptiness():
    stack = []
    assert not stack
    stack.append('one')
    assert bool(stack)  # not not stack

    stack.pop()
    assert not stack


def test_pop_with_stack():
    stack = []
    with pytest.raises(IndexError):
        stack.pop()

