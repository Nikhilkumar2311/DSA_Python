def isPalindrome(n):
    a = n
    result = 0
    while n > 0:
        last = n % 10
        result = result * 10 + last
        n = int(n/10)
    return a == result


num = int(input("Enter The Number: "))
if isPalindrome(num):
    print("Number is Palindrome")
else:
    print("Number is Not Palindrome")
