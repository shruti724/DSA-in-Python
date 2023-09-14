class Node:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None


def search(root, x):
    if root == None:
        return False
    else:
        if root.key == x:
            return True
        elif search(root.left, x) == True:
            return True
        elif search(root.right, x) == True:
            return True
    return False


root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
print(search(root, 50))

