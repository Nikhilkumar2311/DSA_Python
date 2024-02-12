# Program to find Next Greater Element

stack = []
arr = [4, 5, 2, 10, 8]
n = len(arr)

# Array to store the next greater element for each element
ans = [0] * n

# For the last element, there's no greater element, so set it to -1
ans[-1] = -1
stack.append(ans[-1])

# Loop through the array in reverse order
for i in range(n - 2, -1, -1):
    # While the stack is not empty and the top element of the stack is less than or equal to the current element
    while stack and stack[-1] <= arr[i]:
        # Pop elements from the stack until the condition is met
        stack.pop()

    # If the stack becomes empty, there's no greater element
    if not stack:
        ans[i] = -1

    # Otherwise, the next greater element is the top element of the stack
    else:
        ans[i] = stack[-1]

    # Push the current element to the stack
    stack.append(arr[i])

# Print the next greater element for each element in the array
print("Next Greater Element: ", end=' ')
for i in ans:
    print(i, end=' ')
