# Program to find maximum depth/height of Binary Tree

# Basic Tree Structure
class BT:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    # Base case: If the root is None, return 0
    def maxDepth(self, val):
        if not val:
            return 0

        # Recursively calculate the maximum depth of the left subtree
        ls = self.maxDepth(val.left)

        # Recursively calculate the maximum depth of the right subtree
        rs = self.maxDepth(val.right)

        # Return the maximum depth of the current node by adding 1 to the maximum depth of its subtrees
        return 1 + max(ls, rs)


# Create the binary tree
root = BT(1)
root.left = BT(2)
root.right = BT(3)
root.left.left = BT(4)
root.left.right = BT(5)

# Create an object of the Solution class
obj = Solution()

# Calculate the maximum depth of the binary tree
result = obj.maxDepth(root)

# Print the maximum depth
print(f"Max Height: {result}")
