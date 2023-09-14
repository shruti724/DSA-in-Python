class Node:
    def __init__(self,k):
        self.left = None
        self.right = None
        self.key = k


def bst(root,k):
    if root == None:
        return False
    if root.key == k:
        return True
    if root.key < k:
        return bst(root.right, k)
    else:
        return bst(root.left, k)



root = Node(20)
root.left = Node(10)
root.left.left = Node(5)
root.right = Node(40)
root.right.left = Node(30)
root.right.right = Node(80)
root.right.right.left = Node(100)
root.right.right.right = Node(50)
print(bst(root, 30))