class Node:
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None


def insertBeginning(head, x):
    temp = Node(x)
    if head == None:
        return temp
    else:
        temp.next = head
        head.prev = temp
        return temp


def printNode(head):
    curr = head
    while curr != None:
        print(curr.key, end=" ")
        curr = curr.next


head = None
head = insertBeginning(head, 20)
head = insertBeginning(head, 30)
head = insertBeginning(head, 40)
printNode(head)

