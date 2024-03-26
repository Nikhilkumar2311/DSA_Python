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
