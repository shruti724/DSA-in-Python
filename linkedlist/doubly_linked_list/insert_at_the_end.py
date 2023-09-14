class Node:
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None


def insertEnd(head, x):
    temp = Node(x)
    if head == None:
        return temp
    curr = head
    while curr.next != None:
        curr = curr.next
    curr.next = temp
    temp.prev = curr
    return head

def printNode(head):
    curr = head
    while curr != None:
        print(curr.key, end=" ")
        curr = curr.next


head = None
head = insertEnd(head, 20)
head = insertEnd(head, 30)
head = insertEnd(head, 40)
printNode(head)

