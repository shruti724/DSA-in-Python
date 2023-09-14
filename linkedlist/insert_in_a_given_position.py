class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


def insert_at_pos(head, pos, x):
    temp = Node(x)
    if head == None:
        return temp

    if head.next == None:
        head.next = temp
        return head

    curr = head
    currpos = 1
    while curr != None:
        if currpos == pos -1:
            temp.next = curr.next
            curr.next = temp
            return head
        curr = curr.next
        currpos += 1


def printlist(head):
    curr = head
    while curr != None:
        print(curr.key, end=" ")
        curr = curr.next


head = None
head = insert_at_pos(head, 1, 10)
head = insert_at_pos(head, 2, 20)
head = insert_at_pos(head, 3, 30)
head = insert_at_pos(head, 2, 50)
head = insert_at_pos(head, 5, 5)

printlist(head)



