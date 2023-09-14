class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


def delete_kth(head, k):
    if head == None:
        return
    if head.next == None and k == 1:
        return
    currpos = 2
    curr = head.next
    while curr.next != head:
        if k == currpos:
            curr.next = curr.next.next
            return curr.next
        curr = curr.next


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
head = delete_kth(head, 1)
printlist(head)

