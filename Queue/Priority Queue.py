# Priority Queues
n = [2, 4, 10, 9, 7, 11, 1, 14]
if len(n) < 3:
    print("Invalid")
else:
    f = s = t = float('-inf')
    for i in n:
        if i > f:
            t = s
            s = f
            f = i
        elif i > s and i != f:
            t = s
            s = i
        elif i > t and i != f and i != s:
            t = i
    product = f * s * t
    print("Product of the greatest 3 digits: ", product)
