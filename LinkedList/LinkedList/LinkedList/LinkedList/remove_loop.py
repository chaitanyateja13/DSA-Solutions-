class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_loop(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return head

    slow = head
    while slow.next != fast.next:
        slow = slow.next
        fast = fast.next

    fast.next = None
    return head

# Creating list with loop
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = head.next

head = remove_loop(head)

temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")
