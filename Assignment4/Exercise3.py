class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    # Traverse preorder
    def traversePreOrder(self):
        print(self.val, end=' ')
        if self.left:
            self.left.traversePreOrder()
        if self.right:
            self.right.traversePreOrder()

    # Traverse inorder
    def traverseInOrder(self):
        if self.left:
            self.left.traverseInOrder()
        print(self.val, end=' ')
        if self.right:
            self.right.traverseInOrder()

    # Traverse postorder
    def traversePostOrder(self):
        if self.left:
            self.left.traversePostOrder()
        if self.right:
            self.right.traversePostOrder()
        print(self.val, end=' ')

    # Traverse BFS
    def traverseBFS(self):
        queue = [self]  # Start with the root node
        while queue:
            current_node = queue.pop(0)  # Dequeue the first node
            print(current_node.val, end=' ')
            if current_node.left:
                queue.append(current_node.left)  # Enqueue left child
            if current_node.right:
                queue.append(current_node.right)  # Enqueue right child

# Example usage
root = Node(6)
root.left = Node(2)
root.right = Node(8)
root.left.left = Node(1)
root.left.right = Node(4)
root.left.right.left = Node(3)
root.left.right.right = Node(5)
root.right.left = Node(7)
root.right.right = Node(9)

print("Pre order Traversal: ", end="")
root.traversePreOrder()
print("\nIn order Traversal: ", end="")
root.traverseInOrder()
print("\nPost order Traversal: ", end="")
root.traversePostOrder()
print("\nBFS Traversal: ", end="")
root.traverseBFS()
