class MinHeap:
    def __init__(self):
        self.arr = []


def lChild(i):
    return 2*i + 1


def rChild(i):
    return 2*i + 2


def parent(i):
    return (i-1)//2


# root = MinHeap()
print(lChild(1), rChild(1), parent(1))