class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def search(head, key):
    pos = 1
    temp = head
    while temp:
        if temp.data == key:
            return pos
        temp = temp.next
        pos += 1
    return -1

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

print(search(head, 20))
