# Program to implement Circular Queue

# Size of the circular queue
n = 5

# Initialize the circular queue with zeros
arr = [0] * n

# Initialize rear and front pointer to -1
rear = -1
front = -1


def enqueue(ar, x):
    global front, rear
    # If the queue is empty, set front and rear to 0 and insert the element at the rear
    if front == -1 and rear == -1:
        front = rear = 0
        ar[rear] = x
    # If rear has reached the front, queue is full
    elif (rear + 1) % n == front:
        print("Queue is Full")
    else:
        # Increment rear (taking into account circular nature) and insert the element at the rear
        rear = (rear + 1) % n
        ar[rear] = x


def dequeue(ar):
    global front, rear
    # If the queue is empty, print a message indicating so
    if front == -1 and rear == -1:
        print("Queue is empty")
    # If there's only one element in the queue, set front and rear to -1
    elif front == rear:
        front = rear = -1
    else:
        # Remove the element at the front and increment front (taking into account circular nature)
        ar[front] = 0
        front = (front + 1) % n


# Example Usage
enqueue(arr, 1)
enqueue(arr, 2)
enqueue(arr, 3)
enqueue(arr, 4)
enqueue(arr, 6)

print("Original Queue: ", arr)

dequeue(arr)
dequeue(arr)

print("After Removing Element: ", arr)

enqueue(arr, 7)
enqueue(arr, 8)

print("After Adding Element on the removed Element Place: ", arr)

dequeue(arr)

print("After Removing Next Element: ", arr)
