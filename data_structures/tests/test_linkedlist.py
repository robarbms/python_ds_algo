from linkedlist import LinkedList
from node import Node

def getList() -> LinkedList:
    link_list = LinkedList()
    link_list.add(1)
    link_list.add(2)
    link_list.add(3)
    link_list.add(4)
    link_list.add(5)
    return link_list

def test_create_link_list() -> None:
    link_list = LinkedList()
    assert isinstance(link_list, LinkedList)

def test_create_empty_ll() -> None:
    link_list = LinkedList()
    assert link_list.head == None

def test_add() -> None:
    link_list = LinkedList()
    link_list.add(1)
    assert link_list.size() == 1

def test_add_at_index() -> None:
    list = getList()
    list.add(2, 6)
    assert list.size() == 6 and list.get(2).data == 6

def test_remove() -> None:
    list = getList()
    size = list.size()
    list.remove(3)
    assert list.size() == size - 1

def test_remove_none() -> None:
    list = getList()
    size = list.size()
    list.remove(80)
    assert list.size() == size

def test_contains() -> None:
     list = getList()
     assert list.contains(3) == True

def test_contains_none() -> None:
     list = getList()
     assert list.contains(80) == False

def test_get_first() -> None:
    list = getList()
    first = list.getFirst()
    assert first.data == 1

def test_get_last() -> None:
    list = getList()
    last = list.getLast()
    assert last.data == 5

def test_add_first() -> None:
    list = getList()
    list.addFirst(10)
    assert list.head.data == 10

def test_remove_first() -> None:
    list = getList()
    removed = list.removeFirst()
    assert removed.data == 1 and list.head.data == 2 and list.size() == 4

def test_remove_last() -> None:
    list = getList()
    removed = list.removeLast()
    last = list.getLast()
    assert removed.data == 5 and last.data == 4 and list.size() == 4

def test_add_last() -> None:
    list = getList()
    list.addLast(10)
    last = list.getLast()
    assert last.data == 10

def test_add_all() -> None:
    list = LinkedList()
    list.addAll([1,2,3,4,5])
    assert list.size() == 5

def test_add_all_index() -> None:
    list = getList()
    list.addAll(2, [6, 7, 8])
    print(list)
    assert list.size() == 8 and list.get(2).data == 6

def test_add_all_end() -> None:
    list = getList()
    list.addAll([6, 7, 8])
    last = list.getLast()
    assert list.size() == 8 and last.data == 8

def test_add_all_none() -> None:
    list = LinkedList()
    list.addAll([])
    assert list.size() == 0

def test_clear() -> None:
    list = getList()
    list.clear()
    assert list.size() == 0

def test_get() -> None:
    list = getList()
    node = list.get(2)
    assert node.data == 3

def test_get_out_of_bounds() -> None:
    list = getList()
    node = list.get(50)
    assert node == None

def test_set() -> None:
    list = getList()
    list.set(2, 10)
    node = list.get(2)
    assert node.data == 10

def test_set_returned() -> None:
    list = getList()
    node = list.set(2, 10)
    assert node.data == 3

def test_index_of() -> None:
    list = getList()
    index = list.indexOf(3)
    assert index == 2

def test_last_index_of() -> None:
    list = LinkedList()
    list.addAll([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
    index = list.lastIndexOf(5)
    assert index == 9

def test_peek() -> None:
    list = getList()
    peek = list.peek()
    assert peek.data == 1

def test_element() -> None:
    list = getList()
    element = list.element()
    assert element.data == 1

def test_poll() -> None:
    list = getList()
    polled = list.poll()
    assert polled.data == 1 and list.head.data == 2 and list.size() == 4

def test_offer() -> None:
    list = getList()
    offered = list.offer(10)
    last = list.getLast()
    assert last.data == 10 and offered == True

def test_offer_first() -> None:
    list = getList()
    offered = list.offerFirst(10)
    assert list.head.data == 10 and offered == True

def test_offer_last() -> None:
    list = getList()
    offered = list.offerLast(10)
    last = list.getLast()
    assert last.data == 10 and offered == True

def test_peek_first() -> None:
    list = getList()
    peek = list.peekFirst()
    assert peek.data == 1 and list.size() == 5

def test_peek_last() -> None:
    list = getList()
    peek = list.peekLast()
    last = list.getLast()
    assert peek.data == last.data and list.size() == 5

def test_poll_first() -> None:
    list = getList()
    poll = list.pollFirst()
    assert poll.data == 1 and list.head.data == 2 and list.size() == 4

def test_poll_last() -> None:
    list = getList()
    poll = list.pollLast()
    last = list.getLast()
    assert poll.data == 5 and last.data == 4 and list.size() == 4

def test_push() -> None:
    list = getList()
    list.push(10)
    assert list.head.data == 10 and list.size() == 6

def test_pop() -> None:
    list = getList()
    pop = list.pop()
    last = list.getLast()
    assert pop.data == 1 and list.head.data == 2 and list.size() == 4

def test_remove_first_occurence() -> None:
    list = LinkedList()
    list.addAll([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
    list.removeFirstOccurrence(5)
    pos_4 = list.get(4)
    assert list.size() == 9 and pos_4.data == 1

def test_remove_last_occurence() -> None:
    list = LinkedList()
    list.addAll([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
    list.removeLastOccurrence(5)
    last = list.getLast()
    assert list.size() == 9 and last.data == 4

def test_clone() -> None:
    list = getList()
    cloned = list.clone()
    assert cloned.size() == 5 and cloned.head == list.head

def test_to_array() -> None:
    list = getList()
    arry = list.toArray()
    assert len(arry) == 5 and arry[0] == 1

def test___as_node__() -> None:
    list = LinkedList()
    node1 = list.__as_node__(4)
    node = Node(5)
    node2 = list.__as_node__(5)
    assert isinstance(node1, Node) and isinstance(node2, Node)

def test___repr__() -> None:
    list = LinkedList()
    list.add(1)
    assert list.__repr__() == "[Head: 1]"
