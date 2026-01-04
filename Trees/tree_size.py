def size(root):
    if not root:
        return 0
    return 1 + size(root.left) + size(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Size:", size(root))
