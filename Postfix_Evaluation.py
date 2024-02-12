# Program for Postfix Evaluation

# Input String representing a Postfix expression
inp = "23*5+"

# Stack to store operands during evaluation
stack = []

# Iterate Through each character in the input string
for i in inp:
    # Check if the character is a digit
    if i.isdigit():
        # if it's a digit, convert to integer and push onto the stack
        stack.append(int(i))
    else:
        # If it's an operator, pop two operands from the stack
        a = stack.pop()
        b = stack.pop()

        # Perform the operation based on the operator
        if i == '+':
            stack.append(a + b)
        elif i == '-':
            stack.append(a - b)
        elif i == '*':
            stack.append(a * b)
        elif i == '/':
            stack.append(a / b)

# The result of the postfix expression will be the only element left in the stack
print("Postfix Evaluation: ", stack.pop())
