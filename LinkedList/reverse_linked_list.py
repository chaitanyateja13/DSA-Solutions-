class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_list(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev

# Creating list
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

head = reverse_list(head)

temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")
