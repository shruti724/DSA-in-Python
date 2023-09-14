class node:
    def __init__(self, key):
        self.key = key
        self.next = None


def search(head, key):
    curr = head
    position = 1
    while curr != None:
        if curr.key == key:
            return position
        position += 1
        curr = curr.next
    return -1


head = node(10)
head.next = node(20)
head.next.next = node(40)
print(search(head, 40))
