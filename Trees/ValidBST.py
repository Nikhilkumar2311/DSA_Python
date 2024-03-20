class BST:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.prev = None

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

    def isBST(self, cur):
        if cur:
            if not self.isBST(cur.left):
                return False
            if self.prev is not None and self.prev.val >= cur.val:
                return False
            self.prev = cur
            return self.isBST(cur.right)
        return True


obj2 = Solution()
obj1 = None
obj1 = obj2.insert(obj1, 10)
obj1 = obj2.insert(obj1, 6)
obj1 = obj2.insert(obj1, 1)
obj1 = obj2.insert(obj1, 8)
obj1 = obj2.insert(obj1, 12)
obj1 = obj2.insert(obj1, 11)
obj1 = obj2.insert(obj1, 14)

obj3 = None
obj3 = obj2.insert(obj3, 14)
obj3 = obj2.insert(obj3, 15)
obj3 = obj2.insert(obj3, 10)

print("Ist Tree:")
print("Is BST:", obj2.isBST(obj1))
print("IInd Tree:")
print("Is BST:", obj2.isBST(obj3))
