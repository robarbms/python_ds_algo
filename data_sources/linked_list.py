from node import Node

class LinkedList:
    """
    Singly linked list
    """
    head = None

    # Constructs a list containing the elements of the specified collection, in the order they are returned by the collection's iterator.
    # Constructs an empty list of no collection is provided
    def __init__(self, collection=[]):
        for element in collection[::-1]:
            self.addFirst(element)


    # Helper function to ensure that values are converted to nodes
    def __as_node__(element):
        if element is not isinstance(Node):
            element = Node(element)
        return element

    
    # Returns the first element in this list.
    def getFirst(self):
        return self.head
    

    # Returns the last element in this list.
    def getLast(self):
        last = self.head

        while last and last.next_node:
            last = last.next_node

        return last
    

    # Removes and returns the first element from the list.
    def removeFirst(self):
        head = self.head
        self.head = head.next_node
        head.next_node = None
        return head
    

    # Removes and returns the last element from this list
    def removeLast(self):
        next_last = None
        last = self.head

        while last and last.next_node:
            last, next_last = last.next_node, last

        next_last.next_node = None
        return last


    # Inserts the specified element at the beginning of this list.
    def addFirst(self, element):
        element = self.__as_node_(element)
        head, self.head = self.head, element
        if head:
            element.next_node = head
    

    # Appends the specified element to the end of this list.
    # This method is equivalent to add(E)
    def addLast(self, element):
        element = self.__as_node_(element)
        last = self.head
        while last.next_node:
            last = last.next_node
        last.next_node = element


    # Returns true if this list contains the specified element or value.
    def contains(self, element):
        element = self.__as_node_(element)
        current = self.head

        while current:
            if current.data == element.data:
                return True
            current = current.next_node
        
        return False


    # Returns the number of elements in this list.
    def size(self):
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count
    

    # Appends the specified element to the end of this list or to a specified position in the list.
    def add(self, index, element):
        if not element:
            element, index = index, self.size() - 1

        element = self.__as_node_(element)

        if index == 0:
            self.addFirst(element)
        
        elif index == self.size() - 1 or index >= self.size():
            self.addLast(element)
        
        else:
            current = self.head
            idx = 0

            while current:
                if idx + 1 == index:
                    element.next_node, current.next_node = current.next_node, element
                    return True
                current = current.next_node
                idx += 1

    
    # Removes the first occurrence of the specified element from this list, if it is present.
    # If this list does not contain the element, it is unchanged.
    def remove(self, element):
        element = self.__as_node__(element)
        current = self.head

        while current and current.next_node:
            if current.next_node.data == element.data:
                if current.next_node.next_node:
                    current.next_node = current.next_node.next_node
                else:
                    current.next_node = None
                return True
            
        return False



    # Inserts all of the elements in the specified collection at an index or to the end of the list in the order that they are returned by the specified collections iterator
    def addAll(self, index, collection):
        if collection is None:
            collection, index = index, self.size() - 1

        start = self.get(index)
        next = None
        if start:
            next = start.next_node
        element = None
        for element in collection:
            element = self.__as_node_(element)
            if start:
                start.next_node = element
            else:
                self.head = element
            start = element
        if next:
            element.next_node = next


    # Removes all of the elements from this list. The list will be empty aft this call returns.
    def clear(self):
        self.head = None


    # Returns the element at the specified position in this list.
    def get(self, index):
        current = self.head
        idx = 0
        while current:
            if idx == index:
                return current
            current = current.next_node
            idx += 1

        return None
    

    # Replaces the element at the specified position in this list with the specified element.
    def set(self, index, element):
        element = self.__as_node__(element)
        current = self.head
        idx = 0

        if index == 0:
            head = self.head
            self.head, element.next_node, head.next_node = element, head.next_node, None
            return head
        
        while current:
            if idx + 1 == index:
                replaced, current.next_node = current.next_node, element
                element.next_node, replaced.next_node = replaced.next_node, None
                return replaced
            current = current.next_node
            idx += 1
        
        return None

    
    # Returns the index of the first occurrence of the specified element in this list,
    # or -1 if this list does not contain the element.
    def indexOf(self, element):
        element = self.__as_node__(element)
        current = self.head
        index = 0
        while current:
            if current.data == element.data:
                return index
            current = current.next_node
            index += 1

        return -1




    # Returns the index of the last occurrence of the specified element in this list,
    # or -1 if this list does not contain the element.
    def lastIndexOf(self, element):
        element = self.__as_node__(element)
        current = self.head
        index = 0
        found = -1

        while current:
            if current.data == element.data:
                found = index
            current = current.next_node
            index += 1

        return found
    

    # Retrieves, but does not remove, the head (first element) of this list.
    def peek(self):
        return self.getFirst()
    

    # Retrieves, but does not remove, the head (first element) of this list.
    def element(self):
        return self.getFirst()
    

    # Retrieves and removes the head (first element) of this list.
    def poll(self):
        return self.removeFirst()
    

    # Adds the specified element as the tail (last element) of this list.
    def offer(self, element):
        self.addLast(element)
        return True
    

    # Inserts the specified element at the front of this list.
    def offerFirst(self, element):
        self.addFirst(element)
        return True
    

    # Inserts the specified element at the end of this list.
    def offerLast(self, element):
        self.addLast(element)
        return True
    

    # Retrieves, bud does not remove, the first element of this list, or returns null if this list is empty.
    def peekFirst(self):
        return self.head
    

    # Retrieves, but does not remove, the last element of this list, or returns null if the this list is empty.
    def peekLast(self):
        return self.getLast()


    # Retrieves and removes the first element of this list, or returns null if this list is empty.
    def pollFirst(self):
        return self.removeFirst()

    
    # Retrieves and removes the last element of this list, or returns null if this list is empty.
    def pollLast(self):
        return self.removeLast()
    

    # Pushes and element onto the stack represented by this list. In other words, inserts the element at the front of this list.
    def push(self, element):
        self.addFirst(element)


    # Pops an element from the stack represented by this list. In other words, remove and returns the first element of this list.
    def pop(self):
        return self.removeLast()
  
    