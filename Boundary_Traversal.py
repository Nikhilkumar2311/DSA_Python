class treeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


def leftside(root, res):
    if root:
        if root.left:
            res.append(root.val)
            leftside(root.left, res)
        elif root.right:
            res.append(root.right)
            leftside(root.right, res)


def leaf(root, res):
    if root:
        leaf(root.left, res)
        if not root.left and not root.right:
            res.append(root.val)
        leaf(root.right, res)


def rightside(root, res):
    if root:
        if root.right:
            rightside(root.right, res)
        elif root.left:
            rightside(root.left, res)
    if root.right or root.left:
        res.append(root.val)


def boundaryTraversal(root):
    if root:
        res = [root.val]
        leftside(root.left, res)
        leaf(root, res)
        rightside(root.right, res)
        return res


root = treeNode(10)
root.left = treeNode(6)
root.right = treeNode(12)
root.left.left = treeNode(1)
root.left.right = treeNode(8)
root.right.left = treeNode(11)
root.right.right = treeNode(14)

print(boundaryTraversal(root))
