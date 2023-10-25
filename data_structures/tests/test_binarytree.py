from binarytree import BinaryTree
from binaryTreeNode import BinaryTreeNode

def test_create_tree() -> None:
    tree = BinaryTree()

    assert isinstance(tree, BinaryTree)

def test_create_tree_empty() -> None:
    tree = BinaryTree()

    assert tree.root == None

def test_insert() -> None:
    tree = BinaryTree()
    tree.insert(1)

    assert isinstance(tree.root, BinaryTreeNode)
    assert tree.root.value == 1

def test_insert_data() -> None:
    tree = BinaryTree()
    tree.insert(1)

    assert tree.root.value == 1

def test_insert_multiple() -> None:
    tree = BinaryTree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)

    assert tree.root.value == 10

def test_insert_multiple_left() -> None:
    tree = BinaryTree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(3)

    assert tree.root.value == 10
    assert tree.root.left.value == 5
    assert tree.root.left.left.value == 3

def test_contains_value() -> None:
    tree = BinaryTree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(3)

    assert tree.contains(5) == True

def test_doesnt_contain_value() -> None:
    tree = BinaryTree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(3)

    assert tree.contains(8) == False
