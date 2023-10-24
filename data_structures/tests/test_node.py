from node import Node

def test_create_empty_node() -> None:
    node = Node()
    assert isinstance(node, Node)

def test_empty_node_value() -> None:
    node = Node()
    assert node.data == None

def test_create_node_with_value() -> None:
    node = Node(1)
    assert isinstance(node, Node)

def test_node_data_value() -> None:
    node = Node(1)
    assert node.data == 1

def test_node_data_string() -> None:
    node = Node("hello")
    assert node.data == "hello"

def test_adding_node() -> None:
    head = Node(1)
    head.next = Node(2)

    assert isinstance(head.next, Node)

def test_access_next() -> Node:
    head = Node(1)
    head.next = Node(2)

    assert head.next.data == 2

def test_add_empty_next() -> None:
    head = Node(1)
    head.next = Node()

    assert isinstance(head.next, Node)

def test_add_empty_next_value() -> None:
    head = Node(1)
    head.next = Node()

    assert head.next.data == None

def test_node_repr() -> None:
    node = Node("First")

    assert repr(node) == "<Node data: First>"

def test_node_repr_number() -> None:
    node = Node(123)

    assert repr(node) == "<Node data: 123>"
