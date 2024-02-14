# Intersection of list with O(n)

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    @staticmethod
    def getInteractionNode(HeadA, HeadB):
        if HeadA is None or HeadB is None:
            return None
        a, b = HeadA, HeadB
        # If a & b have different lengths, stop the loop after the second iteration
        while a != b:
            # For the end of the first iteration, reset the pointer to the head of another Linked List
            a = HeadB if a is None else a.next  # Traverse List A and jump to List B if it reaches its end
            b = HeadA if b is None else b.next  # Traverse List B and jump to List A if it reaches its end
        # At this point, either a or b points to the intersection node or both are None (no intersection)
        return a


# Creating nodes
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

# Creating First Linked List
headA = node1
node1.next = node2
node2.next = node3  # Intersection Point

# Creating Second Linked List
headB = node4
node4.next = node5
node5.next = node3  # Intersection Point

# Creating Instance of Solution to use the method
solution = Solution()
result = solution.getInteractionNode(headA, headB)

# If there is an intersection, result will be the intersection node
if result:
    print("Intersection at node with value: ", result.val)
else:
    print("No Intersection")
