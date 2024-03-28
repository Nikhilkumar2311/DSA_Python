def Subarray(nums, k):
    if k <= 1:
        return 0
    left, right, count, product = 0, 0, 0, 1
    n = len(nums)

    while right < n:
        product *= nums[right]
        while product >= k:
            product //= nums[left]
            left += 1
        count += 1 + (right-left)
        right += 1
    return count


nums = [10, 5, 2, 6]
k = 100
print(Subarray(nums, k))
