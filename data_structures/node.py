class Node:
    """
    An object for storing a single node of a linked list
    """

    data = None
    next = None
    previous = None

    # initializing a node
    def __init__(self, data) -> None:
        self.data = data

    # printing a node
    def __repr__(self) -> str:
        return "<Node data: %s>" % self.data
