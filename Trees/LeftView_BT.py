class treeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


class Solution:
    def leftSide(self, root, level, res):
        if root is None:
            return
        if len(res) == level:
            res.append(root.val)
        self.leftSide(root.left, level + 1, res)
        self.leftSide(root.right, level + 1, res)
        return res


root = treeNode(1)
root.left = treeNode(2)
root.right = treeNode(3)
root.left.left = treeNode(4)
root.left.right = treeNode(5)
root.right.left = treeNode(6)
root.right.right = treeNode(7)
root.left.left.right = treeNode(8)

res = []
level = 0

sol = Solution()
result = sol.leftSide(root, level, res)
print("Left View of Binary Tree:", result)
