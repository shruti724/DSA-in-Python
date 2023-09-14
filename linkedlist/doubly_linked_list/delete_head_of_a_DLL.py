class Node:
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None


def delHead(head, x):
    if head == None:
        return
    elif head.next == None:
        return
    head = head.next
    head.prev = None
    return head


def printNode(head):
    curr = head
    while curr is not None:
        print(curr.key, end=" ")
        curr = curr.next


head = Node(10)
head.next = Node(20)
head.next.prev = head
head.next.next = Node(30)
head.next.prev = head.next
head = delHead(head, 20)
head = delHead(head, 30)
printNode(head)

