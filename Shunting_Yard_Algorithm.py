# Shunting Yard Algorithm
s = "3 + 4 * 2"
operator = []
output = []
prec = {'+': 1, '-': 1, '*': 2, '/': 2}
for i in s.split():
    if i.isdigit():
        output.append(i)
    else:
        while operator and operator[-1] in prec and prec[i] <= prec[operator[-1]]:
            output.append(operator.pop())
        operator.append(i)

while operator:
    output.append(operator.pop())
result = ' '.join(output)
print("postfix expression: ", result)
