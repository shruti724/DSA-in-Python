class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


def recursive_reversed_list(head):
    # Base case
    if head == None:
        return
    if head.next == None:
        return head
    rest_head = recursive_reversed_list(head.next)
    rest_tail = head.next
    rest_tail.next = head
    head.next = None
    return rest_head


def printlist(head):
    curr = head
    while curr != None:
        print(curr.key, end=" ")
        curr = curr.next


head = Node(10)
head.next = Node(15)
head.next.next = Node(20)
head = recursive_reversed_list(head)
printlist(head)
