class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


def recursive_reversed_linkedlist(curr, prev=None):
    if curr == None:
        return prev

    next = curr.next
    curr.next = prev
    return recursive_reversed_linkedlist(next, curr)


def printlist(head):
    curr = head
    while curr != None:
        print(curr.key, end=" ")
        curr = curr.next


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head = recursive_reversed_linkedlist(head, None)
printlist(head)

