# Program for implementing a MinStack which should support operations like push, pop
class MinStack:
    def __init__(self):
        # Initialize the main stack and the dummy/minStack to keep track of minimum elements
        self.stack = []
        self.minStack = []

    def push(self, val):
        # Push the value onto the main Stack
        self.stack.append(val)
        # Calculate the minimum between the current value and the previous minimum
        # Append the minimum value to the minStack
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self):
        # Pop the top elements from both stacks to maintain consistency
        self.stack.pop()
        self.minStack.pop()

    def getMin(self) -> int:
        # Return the top element of the minStack, which represents the current minimum value
        return self.minStack[-1]

    def top(self) -> int:
        # Return the top element of the main stack
        return self.stack[-1]


# Create an instance of the MinStack class
min_stack = MinStack()

# Push values onto the stack
min_stack.push(3)
min_stack.push(5)
min_stack.push(2)
min_stack.push(1)

# Display the Top and minimum elements
print("Top Element: ", min_stack.top())
print("Minimum element: ", min_stack.getMin())

# Pop an element and display the minimum element after the pop operation
min_stack.pop()
print("After Pop, minimum element: ", min_stack.getMin())
