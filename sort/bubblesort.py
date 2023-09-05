from linkedlist import LinkedList


"""
Bubble sorting of a collection of type List or LinkedList
Returns a sorted collection of the same type as the input type
"""
def bubble_sort(collection):
    # Sorting for a linked list
    if isinstance(collection, LinkedList):
        def swap_nodes(node1, node2, parent = None):
            node1.next, node2.next = node2.next, node1
            if parent:
                parent.next = node2
            else:
                return node2
        for i in range(collection.size()):
            current = collection.head
            if current.data > current.next.data:
                collection.head = swap_nodes(current, current.next)
                current = collection.head
            while current and current.next and current.next.next:
                if current.next.data > current.next.next.data:
                    swap_nodes(current.next, current.next.next, current)
                current = current.next
        return collection

    # sorting for an array
    for i in range(len(collection)):
        for j in range(len(collection) - 1):
            if collection[j] > collection[j + 1]:
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
    return collection


if __name__ == "__main__":
    items = [2, 6, 3, 7, 12, 4, 18, 10, 15, 16, 1, 5, 13, 17, 24, 11, 20, 27, 21, 19, 8, 9, 26, 14, 25, 23, 22]

    ll = LinkedList()
    ll.addAll(items)

    print(ll)
    sorted = bubble_sort(ll)
    print(sorted)


    print(items)
    sorted_array = bubble_sort(items)
    print(sorted_array)
