class treeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


class Solution:
    def isMirror(self, root):
        if root is None:
            return False
        else:
            return self.isSym(root.left, root.right)

    def isSym(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        return self.isSym(right.right, left.left) and self.isSym(right.left, left.right)


root = treeNode(1)
root.left = treeNode(2)
root.right = treeNode(2)
root.left.left = treeNode(4)
root.left.right = treeNode(5)
root.right.left = treeNode(5)
root.right.right = treeNode(4)

sol = Solution()
result = sol.isMirror(root)
print(result)
