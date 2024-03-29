def maxSubArray(nums, k):
    ans = 0
    mp = {}
    l = 0
    n = len(nums)
    for r in range(n):
        mp[nums[r]] = mp.get(nums[r], 0) + 1
        if mp[nums[r]] > k:
            while nums[l] != nums[r]:
                mp[nums[l]] -= 1
                l += 1
            mp[nums[l]] -= 1
            l += 1
        ans = max(ans, r - l + 1)
    return ans


nums = [1, 2, 3, 1, 2, 3, 1, 2]
k = 2
print(maxSubArray(nums, k))
