# Level Order Traversal
class treeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


class Solution:
  def levelOrder(self, root):
    if root is None:
      return
    result = [[root.val]]
    q = []
    q.append(root)
    while q:
      temp = []
      for i in range(len(q)):
        a = q.pop(0)
        if a.left:
          temp.append(a.left.val)
          q.append(a.left)
        if a.right:
          temp.append(a.right.val)
          q.append(a.right)
      if len(temp) > 0:
        result.append(temp)
    return result


root = treeNode(1)
root.left = treeNode(2)
root.right = treeNode(3)
root.left.left = treeNode(4)
root.left.right = treeNode(5)
root.right.left = treeNode(6)
root.right.right = treeNode(7)

level = Solution()
print("Level Order Traversal: ")
print(level.levelOrder(root))
