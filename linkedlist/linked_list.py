class node:
    def __init__(self, key):
        self.key = key
        self.next = None


def printList(head):
    curr = head
    while curr != None:
        print(curr.key, end=" ")
        curr = curr.next


head = node(10)
head.next = node(30)
head.next.next = node(20)
printList(head)









