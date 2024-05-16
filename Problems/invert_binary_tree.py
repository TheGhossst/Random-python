class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._insert_recursive(self.root, val)
    
    def _insert_recursive(self, node, val):
        if val < node.val:
            if node.left:
                self._insert_recursive(node.left, val)
            else:
                node.left = TreeNode(val)
        else:
            if node.right:
                self._insert_recursive(node.right, val)
            else:
                node.right = TreeNode(val)
                
    def print_tree(self,node, level=0):
        if node is not None:
            self.print_tree(node.right, level + 1)
            print(' ' * 4 * level + '->', node.val)
            self.print_tree(node.left, level + 1)


    def invert(self,node):
        if node:
            left = node.left
            right = node.right
            
            node.left = right
            node.right = left
            
            self.invert(node.left)
            self.invert(node.right)
            
        return node
        

tree = BinaryTree()
tree.insert(4)
tree.insert(2)
tree.insert(7)
tree.insert(1)
tree.insert(3)
tree.insert(6)
tree.insert(9)
print("Original tree:")
tree.print_tree(tree.root)

tree.invert(tree.root)
print("\nInverted tree:")
tree.print_tree(tree.root)
