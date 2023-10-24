from queue import Queue
from node import Node

def test_create_queue() -> None:
    que = Queue()

    assert isinstance(que, Queue)

def test_create_empty_queue() -> None:
    que = Queue()

    assert que.length == 0

def test_enqueue() -> None:
    que = Queue()
    que.enqueue(1)

    assert que.length == 1

def test_peek() -> None:
    que = Queue()
    que.enqueue(1)
    peeked = que.peek()

    assert isinstance(peeked, Node)

def test_peek_value() -> None:
    que = Queue()
    que.enqueue(1)
    peeked = que.peek()

    assert peeked.data == 1

def test_peek_first() -> None:
    que = Queue()
    que.enqueue(1)
    que.enqueue(2)
    peeked = que.peek()

    assert peeked.data == 1

def test_dequeue() -> None:
    que = Queue()
    que.enqueue(1)
    que.enqueue(2)
    que.enqueue(3)
    deque = que.dequeue()

    assert isinstance(deque, Node)

def test_dequeue_value() -> None:
    que = Queue()
    que.enqueue(1)
    que.enqueue(2)
    que.enqueue(3)
    deque = que.dequeue()

    assert deque.data == 1