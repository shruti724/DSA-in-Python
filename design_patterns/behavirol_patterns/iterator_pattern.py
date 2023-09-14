class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self, head):
        self.head = head
        self.cur = None

    # Define Iterator
    def __next__(self):
        if self.cur:
            val = self.cur.val
            self.cur = self.cur.next
            return val
        else:
            raise StopIteration


# Initialize LinkedList
head = LinkedList(1)
head.next = LinkedList(2)
head.next.next = LinkedList(3)
myList = LinkedList(head)

# Iterate through LinkedList
for n in myList:
    print(n)

