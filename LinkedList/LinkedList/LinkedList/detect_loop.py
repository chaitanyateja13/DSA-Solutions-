class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def detect_loop(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = head  # creating loop

print(detect_loop(head))
