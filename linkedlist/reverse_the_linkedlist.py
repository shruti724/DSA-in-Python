class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


def reverse_the_Linkedlist(head):
    curr = head
    prev = None

    while curr != None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev


def printlist(head):
    curr = head
    while curr != None:
        print(curr.key, end=" ")
        curr = curr.next


# head = None
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head = reverse_the_Linkedlist(head)
printlist(head)
