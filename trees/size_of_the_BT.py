class Node:
    def __init__(self, k):
        self.left = None
        self.right = None
        self.key = k


def size_of_tree(root):

    if root == None:
        return 0
    else:
        ls = size_of_tree(root.left)
        rs = size_of_tree(root.right)
        return ls + rs + 1


root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
print(size_of_tree(root))

