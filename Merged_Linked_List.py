# Merge two sorted linked lists

"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def new(arr):
    # Function to create a linked list from a list
    if not arr:
        return None
    # Create the head node with the first element of the list
    head = Node(arr[0])
    current = head
    # Iterate through the list to create the linked list
    for data in arr[1:]:
        current.next = Node(data)  # Create a new node with current data
        current = current.next  # Move to the next node
    return head  # Return the head of the linked list


def merge(ar1, ar2):
    # Pointer to the current node in the first linked list
    t1 = ar1

    # Pointer to the current node in the second linked list
    t2 = ar2

    # Dummy node to hold the merged list
    dummy_node = Node(-1)
    temp = dummy_node

    # Loop until either of the linked lists becomes empty
    while t1 is not None and t2 is not None:
        if t1.data < t2.data:  # If data in the first list is smaller
            temp.next = t1  # Link the current node from the first list
            t1 = t1.next  # Move to the next node in the first list
        else:  # If data in the second list is smaller or equal
            temp.next = t2  # Link the current node from the second list
            t2 = t2.next  # Move to the next node in the second list
        temp = temp.next  # Move the temporary pointer

    # Add any remaining nodes from the first or second list
    if t1:
        temp.next = t1
    else:
        temp.next = t2

    return dummy_node.next  # Return the head of the merged list


def print_list(head):
    current = head
    while current:
        print(current.data, end=' ')  # Print current node's data
        current = current.next  # Move to the next node
    print()


# Main Function
list1 = [1, 3, 4, 5, 8]
l1 = new(list1)
list2 = [2, 6, 8, 10, 12, 15]
l2 = new(list2)
merged = merge(l1, l2)
print_list(merged)
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def new(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for data in arr[1:]:
        current.next = Node(data)
        current = current.next
    return head


def merge(ar1, ar2):
    t1 = ar1
    t2 = ar2
    dummy_node = Node(-1)
    temp = dummy_node
    while t1 is not None and t2 is not None:
        if t1.data < t2.data:
            temp.next = t1
            t1 = t1.next
        else:
            temp.next = t2
            t2 = t2.next
        temp = temp.next
    if t1:
        temp.next = t1
    else:
        temp.next = t2
    return dummy_node.next


def print_list(head):
    current = head
    while current:
        print(current.data, end=' ')
        current = current.next
    print()


list1 = list(map(int, input("Enter the elements of the first list: ").split()))
l1 = new(list1)
list2 = list(map(int, input("Enter the elements of the second list: ").split()))
l2 = new(list2)
merged = merge(l1, l2)
print_list(merged)
