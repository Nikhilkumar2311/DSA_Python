# Program to find the lowest common ancestor
"""
# Basic Tree Structure
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def lowestAncestor(self, val, a, b):
        # If the current node is None or matches either of the given nodes, return the current node
        if not val or val == a or val == b:
            return val

        # Recursively find the lowest common ancestor in the left and right subtrees
        left = self.lowestAncestor(val.left, a, b)
        right = self.lowestAncestor(val.right, a, b)

        # If both left and right subtrees have a common ancestor, the current node is the LCA
        if left and right:
            return val

        # If one of the subtrees has a common ancestor, propagate it upwards
        return left or right


# Create the tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Create an instance of the Solution class
lca = Solution()

# Define the nodes for which we want to find the lowest common ancestor
p = root.left.left
q = root.left.right

# Find the lowest common ancestor
result = lca.lowestAncestor(root, p, q)

# Print the result
print(f"Lowest Common Ancestor: {result.val}")
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def lowestAncestor(self, val, a, b):
        if not val or val == a or val == b:
            return val

        left = self.lowestAncestor(val.left, a, b)
        right = self.lowestAncestor(val.right, a, b)

        if left and right:
            return val

        return left or right


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

lca = Solution()

p = root.left.left
q = root.left.right

result = lca.lowestAncestor(root, p, q)

print(f"Lowest Common Ancestor: {result.val}")
