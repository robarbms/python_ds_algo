from node import Node

class Stack:
    """
    A stack class
    """

    top: Node = None
    bottom: Node = None
    length: int = 0

    # Initializing a Stack
    def __init__(self) -> None:
        pass

    def __repr__(self) -> str:
        string: str = ""
        start: Node = self.top
        while start != None:
            string += repr(start)
            start = start.next
            if start != None:
                string += " -> "
        return string

    # Returns the top node that will be returned for a pop    
    def peek(self) -> Node:
        return self.top
    
    # Pushes a new value to the stack
    def push(self, value) -> None:
        newNode: Node = Node(value)
        [newNode.next, self.top] = [self.top, newNode]
        self.length += 1
        return self
        
    # Pops the last node added
    def pop(self) -> Node:
        popNode: Node = self.top
        self.top = popNode.next
        self.length -= 1
        return popNode

