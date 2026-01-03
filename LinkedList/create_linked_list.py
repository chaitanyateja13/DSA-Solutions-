class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creating nodes
head = Node(10)
second = Node(20)
third = Node(30)

# Linking nodes
head.next = second
second.next = third

# Traversing linked list
temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")
