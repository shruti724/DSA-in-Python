class Node:
    def __init__(self, k):
        self.left = None
        self.right = None
        self.key = k


def printtree(root):
    if root == None:
        return
    print(root.key, end=" ")
    printtree(root.left)
    printtree(root.right)


root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root = printtree(root)
