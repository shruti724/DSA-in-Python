class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


def insert_at_beginning(head, x):
    temp = Node(x)
    if head == None:
        temp.next = temp
        return temp
    temp.next = head.next
    head.next = temp
    head.key, temp.key = temp.key, head.key
    return head


def printlist(head):
    print(head.key, end=" ")
    curr = head.next
    while curr != head:
        print(curr.key, end=" ")
        curr = curr.next


head = Node(5)
head.next = Node(10)
head.next.next = Node(15)
head.next.next.next = head
head = insert_at_beginning(head, 24)
printlist(head)
