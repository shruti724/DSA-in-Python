class Node:
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None


def printNode(head):
    curr = head
    while curr != None:
        print(curr.key, end=" ")
        curr = curr.next


head = Node(10)
head.next = Node(20)
head.next.prev = head
head.next.next = Node(30)
head.next.prev = head.next
printNode(head)

