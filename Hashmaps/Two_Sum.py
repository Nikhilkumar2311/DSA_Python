# Two Sum
"""
i/p [2,4,5,6] Target = 9
o/p  [1,2] These are indexes of the numbers

check if
dif = Target - num
if dif in mapds:
  print(index of 4 and 5)

here 2,4,5,6 are iteratives
and 0,1,2,3 are indexes
enumerate keyword retuns the iterative and index
"""

arr = [2, 4, 6, 5]
target = 9
dic = {}
for index, num in enumerate(arr):
    diff = target - num
    if diff in dic:
        print(f"[{dic[diff]}, {index}]")
        break
    dic[num] = index

# for i in arr:
#     diff = target - i
#     if diff in arr:
#         print(i, diff)
#         break
