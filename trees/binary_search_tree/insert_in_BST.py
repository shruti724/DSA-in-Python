class Node:
    def __init__(self,k):
        self.left = None
        self.right = None
        self.key = k


def iter_bst(root,k):
    while root != None:
        if root.key == k:
            return True
        if root.key > k:
            root = root.left
        else:
            root = root.right
    return False


root = Node(20)
root.left = Node(10)
root.left.left = Node(5)
root.right = Node(40)
root.right.left = Node(30)
root.right.right = Node(80)
root.right.right.right = Node(100)
root.right.right.left = Node(50)
print(iter_bst(root, 50))