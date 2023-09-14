class Node:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None


def height(root):
    if root == None:
        return False
    else:
        ls = height(root.left)
        rs = height(root.right)
    return max(ls, rs) + 1


root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
print(height(root))

