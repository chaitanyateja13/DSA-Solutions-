class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def is_palindrome(head):
    values = []
    temp = head
    while temp:
        values.append(temp.data)
        temp = temp.next

    return values == values[::-1]

head = Node(1)
head.next = Node(2)
head.next.next = Node(2)
head.next.next.next = Node(1)

print(is_palindrome(head))
