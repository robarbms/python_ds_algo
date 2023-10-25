"""
Class representing a node used in trees
"""

class TreeNode:
    children = []

    def __init__(self, value):
        self.data = value

    def add(self, node):
        self.children.push(node)
        return self