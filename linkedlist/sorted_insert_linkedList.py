class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


def sorted_insert(head, x):
    curr = head
    temp = Node(x)
    if head == None:
        return Node(x)
    if curr.next == None:
        curr.next = Node(x)
        return head
    if head.key > x:
        temp.next = head
        return temp
    while curr != None:
        if curr.key < x and curr.next.key > x:
            temp.next = curr.next
            curr.next = temp
            return head
        curr = curr.next


def printList(head):
    curr = head
    while curr != None:
        print(curr.key, end=" ")
        curr = curr.next


# head = None
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(50)
head = sorted_insert(head, 5)
printList(head)
