class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


def reverse_linkedlist(head):
    stack = []
    curr = head
    while curr != None:
        stack.append(curr.key)
        curr = curr.next
    curr = head
    while curr != None:
        curr.key = stack.pop()
        curr = curr.next
    return head


def printlist(head):
    curr = head
    while curr != None:
        print(curr.key, end=" ")
        curr = curr.next


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head = reverse_linkedlist(head)
printlist(head)
