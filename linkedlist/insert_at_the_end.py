class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


def inserAtend(head, x):
    if head == None:
        return Node(x)
    curr = head
    while curr.next != None:
        curr = curr.next
    curr.next = Node(x)
    return head


def printlist(head):
    curr = head
    while curr != None:
        print(curr.key, end=" ")
        curr = curr.next


head = None
head = inserAtend(head, 20)
head = inserAtend(head, 40)
printlist(head)


