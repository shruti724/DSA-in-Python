class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


def delete_from_end(head):
    if head == None:
        return
    if head.next == None:
        return
    curr = head
    while curr.next.next != None:
        curr = curr.next
    curr.next = None
    return head


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
head = delete_from_end(head)
printlist(head)
