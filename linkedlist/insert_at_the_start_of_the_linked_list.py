class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


def insert_at_the_start(head, x):
    temp = Node(x)
    temp.next = head
    return temp


def printlist(head):
    curr = head
    while curr != None:
        print(curr.key, end=" ")
        curr = curr.next


head = None
head = insert_at_the_start(head, 10)
head = insert_at_the_start(head, 20)
head = insert_at_the_start(head, 30)
printlist(head)

