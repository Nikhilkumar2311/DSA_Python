nums = [1, 2, 3, 4, 2]
slow, fast = nums[0], nums[0]
while True:
    slow = nums[slow]
    fast = nums[nums[fast]]
    if slow == fast:
        break
fast = nums[0]
while slow != fast:
    slow = nums[slow]
    fast = nums[fast]
print(slow)
