# Swap Nodes Pairwise
"""
input : 1->2->3->4
output : 2->1->4->3
input2 : 1->2->3
output2 : 2->1->3

head is the pointer which points the first node
temp = head
while(temp!=null) # used to traverse the linked list till end
"""

"""
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def swapPairs(self, head):
        # Create a dummy node to ease things
        dummy = Node(0)
        dummy.next = head       # with dummy node list is: 0->1->2->3->4
        temp = dummy     #create the pointer for swapping the node values  is "point" and assign it to the dummy
        # Ensure nodes we are swapping are not None
        while temp.next and temp.next.next:
            # Identify nodes to swap
            swap1 = temp.next
            swap2 = temp.next.next
            # Actually swap
            swap1.next = swap2.next
            swap2.next = swap1
            temp.next = swap2
             # Prepare for the next iteration
            temp = swap1
        return dummy.next
# Create the linked list 1->2->3->4
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

# Create a Solution object
solution = Solution()

# Call the swapPairs function
swapped_head = solution.swapPairs(head)

# Print the swapped linked list
current = swapped_head
while current is not None:
    print(current.val, end="")
    if current.next is not None:
        print("->", end="")
    current = current.next
"""

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        dummy = Node(0)
        dummy.next = head
        temp = dummy
        while temp.next and temp.next.next:
            swap1 = temp.next
            swap2 = temp.next.next
            swap1.next = swap2.next
            swap2.next = swap1
            temp.next = swap2
            temp = swap1
        return dummy.next

def printLinkedList(head):
    current = head
    while current is not None:
        print(current.val, end="")
        if current.next is not None:
            print("->", end="")
        current = current.next
    print()

original_head = Node(10)
original_head.next = Node(20)
original_head.next.next = Node(30)
original_head.next.next.next = Node(40)
original_head.next.next.next.next = Node(50)

print("Original Linked List:")
printLinkedList(original_head)

solution = Solution()

swapped_head = solution.swapPairs(original_head)

print("Swapped Linked List:")
printLinkedList(swapped_head)
