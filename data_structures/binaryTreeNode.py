from typing import Self

class BinaryTreeNode:
    left: Self = None
    right: Self = None

    def __init__(self, value) -> None:
        self.value = value

