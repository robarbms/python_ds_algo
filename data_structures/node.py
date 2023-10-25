class Node:
    """
    An object for storing a single node of a data structure
    """

    data = None
    next = None

    # initializing a node
    def __init__(self, data = None) -> None:
        self.data = data

    # printing a node
    def __repr__(self) -> str:
        return "<Node data: %s>" % self.data
