from stack import Stack
from node import Node

def test_create_stack() -> None:
    newStack = Stack()

    assert newStack.length == 0

def test_push() -> None:
    newStack = Stack()
    newStack.push(1)

    assert newStack.length == 1

def test_peek() -> None:
    newStack = Stack()
    newStack.push(1)
    peeked = newStack.peek()
    
    assert isinstance(peeked, Node)

def test_peek_value() -> None:
    newStack = Stack()
    newStack.push(1)
    peeked = newStack.peek()

    assert peeked.data == 1

def test_peek_last() -> None:
    newStack = Stack()
    newStack.push(1)
    newStack.push(2)
    newStack.push(3)
    peeked = newStack.peek()

    assert peeked.data == 3

def test_pop() -> None:
    newStack = Stack()
    newStack.push(1)
    newStack.pop()

    assert newStack.length == 0

def test_pop_returns_node() -> None:
    newStack = Stack()
    newStack.push(1)
    popped = newStack.pop()

    assert isinstance(popped, Node)

def test_pop_return_value() -> None:
    newStack = Stack()
    newStack.push("first")
    newStack.push("second")
    newStack.push("third")
    popped = newStack.pop()

    assert popped.data == "third"

def test_stack_print() -> None:
    newStack = Stack()
    newStack.push("first")
    newStack.push("second")
    newStack.push("third")

    assert repr(newStack) == "<Node data: third> -> <Node data: second> -> <Node data: first>"