"""

Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that
the resulting parentheses string is valid and return any valid string.
Formally, a parentheses string is valid if and only if:
It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"

Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.

"""


def minRemoveToMakeValid(s: str):
    left_count = 0
    right_count = 0
    stack = []

    # Pass 1
    for ch in s:
        if ch == '(':
            left_count += 1
        elif ch == ')':
            right_count += 1
        if right_count > left_count:
            right_count -= 1
        else:
            stack.append(ch)

    result = ""

    # Pass 2
    while stack:
        current_char = stack.pop()
        if left_count > right_count and current_char == '(':
            left_count -= 1
        else:
            result += current_char

    # Reverse the result string
    return result[::-1]


str1 = "lee(t(c)o)de)"
print(minRemoveToMakeValid(str1))
