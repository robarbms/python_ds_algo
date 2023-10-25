from binaryTreeNode import BinaryTreeNode

"""
Class for creating binary trees
"""
class BinaryTree:
    root: BinaryTreeNode = None

    # This logic isn't quite right
    def insert(self, value, node=None) -> None:
        if self.root == None:
            self.root = BinaryTreeNode(value)
            return
        
        if node == None:
            node = self.root
        
        if value < node.value:
            if node.left == None:
                node.left = BinaryTreeNode(value)
            else:
                self.insert(value, node.left)
        else:
            if node.right == None:
                node.right = BinaryTreeNode(value)
            else:
                self.insert(value, node.right)
    
    def contains(self, value, node = None) -> bool:
        if node == None:
            node = self.root
        
        if value == node.value:
            return True
        
        if value < node.value:
            if node.value == None:
                return False
            else:
                return self.contains(value, node.left)
        else:
            if node.right == None:
                return False
            else:
                return self.contains(value, node.right)
