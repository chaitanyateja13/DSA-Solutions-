class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_node(head, key):
    if head and head.data == key:
        return head.next

    temp = head
    while temp.next and temp.next.data != key:
        temp = temp.next

    if temp.next:
        temp.next = temp.next.next

    return head

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

head = delete_node(head, 20)

temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")
