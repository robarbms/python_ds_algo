from binarytree import BinaryTree
from node import Node

def test_create_tree() -> None:
    tree = BinaryTree()

    assert isinstance(tree, BinaryTree)

def test_create_tree_empty() -> None:
    tree = BinaryTree()

    assert tree.head == None

def test_insert() -> None:
    tree = BinaryTree()
    tree.insert(1)

    assert isinstance(tree.head, Node)

def test_insert_data() -> None:
    tree = BinaryTree()
    tree.insert(1)

    assert tree.head.data == 1

def test_insert_multiple() -> None:
    tree = BinaryTree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)

    assert tree.head.data == 10

def test_insert_multiple_left() -> None:
    tree = BinaryTree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(7)

    assert tree.head.data == 10
    assert tree.head.previous.data == 5
    assert tree.head.previous.next.data == 7

