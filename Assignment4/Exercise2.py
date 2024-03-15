# Traverse Binary Tree in Python using DFS 

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    # Traverse inorder
    def traverseInOrder(self):
        if self.left:
            self.left.traverseInOrder()
        print(self.val, end=' ')
        if self.right:
            self.right.traverseInOrder()

# TREE 1
root1 = Node("A")

root1.left = Node("B")
root1.right = Node("C")

root1.left.left = Node("D")
root1.left.right = Node("E")

root1.left.right.left = Node("H")
root1.left.right.right = Node("I")

root1.right.left = Node("F")
root1.right.right = Node("G")

print("\nIn order Traversal for Tree 1: ", end="")
root1.traverseInOrder()

print("\n--------------------------\n")

# TREE 2
root2 = Node("A")

root2.left = Node("B")
root2.right = Node("C")

root2.right.left = Node("D")
root2.right.right = Node("E")

root2.right.right.left = Node("F")
root2.right.right.right = Node("G")

print("\nIn order Traversal for Tree 2: ", end="")
root2.traverseInOrder()

print("\n--------------------------\n")
