class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

head = Node(20)
head = insert_beginning(head, 10)

temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")
