from typing import Self
from node import Node
class Queue:
    """
    Class for creating and managing queues
    """
    first = None
    last = None
    length = 0

    def __init__(self) -> None:
        pass

    def __repr__(self) -> str:
        string = ""
        start = self.first
        while start is not None:
            string += repr(start)
            if start.next is not None:
                string += " -> "
            start = start.next

    def peek(self) -> Node:
        return self.first
    
    def enqueue(self, value) -> Self:
        newNode = Node(value)
        if self.length == 0:
            self.first = newNode
        else:
            self.next = newNode
        self.last = newNode
        self.length += 1
        return self

    def dequeue(self) -> Node:
        if self.length > 0:
            self.length -= 1
            dequeued = self.first
            self.first = dequeued.next
            return dequeued
        return None

    def empty(self) -> Node:
        return self.length > 0