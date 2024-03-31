"""

Given an integer array nums of length n where all the integers of nums are in the range [1, n]
and each integer appears once or twice, return an array of all the integers that appears twice.
You must write an algorithm that runs in O(n) time and uses only constant extra space.

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
Example 2:

Input: nums = [1,1,2]
Output: [1]
Example 3:

Input: nums = [1]
Output: []

"""

nums = [1, 2, 4, 2, 3, 4, 1]
ans = []
if len(nums) > 1:
    sortl = sorted(nums)
    i = 1
    while i < len(sortl):
        if sortl[i] == sortl[i - 1]:
            ans.append(sortl[i])
        i += 1
print(ans)
