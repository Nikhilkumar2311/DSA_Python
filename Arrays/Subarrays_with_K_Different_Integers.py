"""

Given an integer array nums and an integer k, return the number of good subarrays of nums.
A good array is an array where the number of different integers in that array is exactly k.
For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.

Example 1:

Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2],
[1,2,1,2]
Example 2:

Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].

"""


def subarraysWithKDistinct(nums, k):
    return subarraysWithAtMostKDistinct(nums, k) - subarraysWithAtMostKDistinct(nums, k - 1)


def subarraysWithAtMostKDistinct(nums, k):
    ans = 0
    count = [0] * (len(nums) + 1)

    l = 0
    for r in range(len(nums)):
        count[nums[r]] += 1
        if count[nums[r]] == 1:
            k -= 1
        while k == -1:
            count[nums[l]] -= 1
            if count[nums[l]] == 0:
                k += 1
            l += 1
        ans += r - l + 1
    return ans


nums = [1, 2, 1, 2, 3]
k = 2
print(subarraysWithKDistinct(nums, k))
