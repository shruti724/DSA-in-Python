from collections import deque

class Node:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None


def iter_preorder(root):
    if root == None:
        return
    q = deque()
    q.append(root)
    while len(q) > 0:
        node = q.popleft()
        print(node.key, end=" ")
        if node.left != None:
            q.append(node.left)
        if node.right != None:
            q.append(node.right)

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
iter_preorder(root)


