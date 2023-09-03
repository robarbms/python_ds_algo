class Node:
    """
    An object for storing a single node of a linked list
    """

    data = None
    next_node = None

    # initializing a node
    def __init__(self, data):
        self.data = data

    # printing a node
    def __repr__(self):
        return "<Node data: %s>" % self.data
