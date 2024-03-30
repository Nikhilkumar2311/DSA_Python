def arrays(nums, k):
    max_val = max(nums)
    ans = 0
    l = 0
    c = 0
    for num in nums:
        if num == max_val:
            c += 1
        while c >= k:
            if nums[l] == max_val:
                c -= 1
            l += 1
        ans += l
    return ans


nums = [1, 3, 2, 3, 3]
k = 2
print(arrays(nums, k))
