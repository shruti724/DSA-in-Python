class Node:
    def __init__(self,key):
        self.key = key
        self.next = None


def delete_head(head):
    if head == None:
        return
    if head.next == head:
        return None
    curr = head
    while curr.next != head:
        curr = curr.next
    curr.next = head.next
    return curr.next


def printlist(head):
    if head == None:
        return
    if head.next == head:
        return None
    print(head.key, end=" ")
    curr = head.next
    while curr != head:
        print(curr.key, end=" ")
        curr = curr.next


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = head
# head.next = head
head = delete_head(head)
printlist(head)

