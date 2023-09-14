class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


# def insert_at_beginning(head, x):
#    temp = Node(x)
#    if head == None:
#        temp.next = temp
#        return temp
#    print(temp.key, end=" ")
#    print(head.key, end=" ")
#    curr = head.next
#    while curr != head:
#        print(curr.key, end=" ")
#        curr = curr.next

def insert_at_beginning(head, x):
    temp = Node(x)
    if head == None:
        temp.next = temp
        return temp
    curr = head
    while curr.next != head:
        curr = curr.next
    curr.next = temp
    temp.next = head
    return temp


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
