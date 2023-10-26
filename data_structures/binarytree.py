from binaryTreeNode import BinaryTreeNode

"""
Class for creating binary trees
"""
class BinaryTree:
    root: BinaryTreeNode = None

    # This logic isn't quite right
    def insert(self, value, node=None) -> None:
        newNode: BinaryTreeNode = BinaryTreeNode(value)
        if self.root == None:
            self.root = newNode
            return
        
        if node == None:
            node = self.root
        
        if value < node.value:
            if node.left == None:
                node.left = newNode
            else:
                self.insert(value, node.left)
        else:
            if node.right == None:
                node.right = newNode
            else:
                self.insert(value, node.right)
    
    def lookup(self, value, node = None) -> BinaryTreeNode | bool:
        if node == None:
            node = self.root
        
        if value == node.value:
            return node
        
        if value < node.value:
            if node.value == None:
                return False
            else:
                return self.lookup(value, node.left)
        else:
            if node.right == None:
                return False
            else:
                return self.lookup(value, node.right)
            
    def remove(self, value):
        if self.root == None:
            return
        prev = None
        curr = self.root
        while curr.value != value:
            if curr.value > value:
                if curr.left == None:
                    return
                [curr, prev] = [curr.left, curr]
            else:
                if curr.right == None:
                    return
                [curr, prev] = [curr.right, curr]
        
        right = curr.right
        left = curr.right.left

        if curr == self.root:
            self.root = right
