class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_end(head, data):
    new_node = Node(data)
    if head is None:
        return new_node

    temp = head
    while temp.next:
        temp = temp.next
    temp.next = new_node
    return head

head = Node(10)
head = insert_end(head, 20)
head = insert_end(head, 30)

temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")
