# Build BST
class BST:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def insert(self, cur, val):
        if cur is None:
            return BST(val)
        if val < cur.val:
            cur.left = self.insert(cur.left, val)
        else:
            cur.right = self.insert(cur.right, val)
        return cur

    def preOrder(self, cur):
        if cur:
            print(cur.val, end=" ")
            self.preOrder(cur.left)
            self.preOrder(cur.right)


obj2 = Solution()
obj1 = None
obj1 = obj2.insert(obj1, 10)
obj1 = obj2.insert(obj1, 6)
obj1 = obj2.insert(obj1, 1)
obj1 = obj2.insert(obj1, 8)
obj1 = obj2.insert(obj1, 12)
obj1 = obj2.insert(obj1, 11)
obj1 = obj2.insert(obj1, 14)


print(obj2.preOrder(obj1))
