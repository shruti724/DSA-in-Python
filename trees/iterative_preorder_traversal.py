class Node:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None


def iter_preorder(root):
    if root == None:
        return
    stack = [root]
    while len(stack)>0:
        curr = stack.pop()
        print(curr.key, end=" ")
        if curr.right != None:
            stack.append(curr.right)
        if curr.left != None:
            stack.append((curr.left))


root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
iter_preorder(root)


