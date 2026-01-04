class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, key):
    if not root:
        return BSTNode(key)
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def search(root, key):
    if not root:
        return False
    if root.data == key:
        return True
    elif key < root.data:
        return search(root.left, key)
    else:
        return search(root.right, key)

root = None
keys = [50, 30, 20, 40, 70, 60, 80]
for key in keys:
    root = insert(root, key)

print(search(root, 60))  # True
print(search(root, 25))  # False
