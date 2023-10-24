from node import Node

"""
Class for creating binary trees
"""
class BinaryTree:
    head: Node = None

    def __init__(self):
        pass

    # This logic isn't quite right
    def insert(self, data, node=None) -> None:
        if node == None:
            node = self.head
            if node == None:
                self.head = Node(data)
            else:
                self.insert(data, self.head)
        else:
            if data < node.data:
                if node.previous == None:
                    node.previous = Node(data)
                else:
                    self.insert(data, node.previous)
            else:
                if node.next == None:
                    node.next = Node(data)
                else:
                    self.insert(data, node.next)
    
    def contains(self, data, node = None):
        if node == None:
            node = self.head
        
        if data == node.data:
            return True
        
        if data < node.data:
            if node.previous == None:
                return False
            else:
                return self.contains(data, node.previous)
        else:
            if node.next == None:
                return False
            else:
                return self.contains(data, node.next)
            
    def toArray(self):
        arr = []
        node = self.head

        def traverse(node):
            if node!= None:
                traverse(node.previous)
                arr.append(node.data)
                traverse(node.next)
        traverse(node)
        return arr
            
            
    def __repr__(self):
        arr = self.toArray()
        str = ""
        for i in arr:
            if str != "":
                str += " "
            str += "%s" % i

        return str


tree = BinaryTree()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(2)
tree.insert(1)
tree.insert(12)
tree.insert(11)
tree.insert(4)

print(tree)

print(tree.contains(10))
print(tree.contains(6))

