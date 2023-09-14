class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


def printlist(head):
    if head == None:
        return
    print(head.key, end=" ")
    curr = head.next
    while curr != head:
        print(curr.key, end=" ")
        curr = curr.next



head = Node(5)
head.next = Node(10)
head.next.next = Node(15)
head.next.next.next = Node(20)
head.next.next.next.next = head
printlist(head)
