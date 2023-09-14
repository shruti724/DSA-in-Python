class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


def deleteNode(llist, position):
    if llist == None:
        return
    curr_pos = 0
    curr = llist
    while curr.next != None:
        if curr_pos == position - 1:
            curr.next = curr.next.next
            return llist
        curr_pos += 1
        curr = curr.next

def printlist(head):
    curr = head
    while curr != None:
        print(curr.key, end=" ")
        curr = curr.next
    print()


head = Node(10)
head.next = Node(60)
head.next.next = Node(30)
head.next.next.next = Node(40)
head = deleteNode(head, 2)
printlist(head)
