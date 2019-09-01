nums = [0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 4, 5, 6, 6, 6, 7, 8, 8]
target = 4

l = len(nums)
res = [-1, -1]


def deep(ls, start):
    print(ls)
    print(start)
    if not ls:
        return
    center = (len(ls) + 1) // 2 - 1
    if ls[center] == target:
        index = start + center
        res[0] = index
        res[1] = index
        while res[0] - 1 >= 0 and nums[res[0] - 1] == target:
            res[0] = res[0] - 1
        while res[1] + 1 < len(nums) and nums[res[1] + 1] == target:
            res[1] = res[1] + 1
    elif ls[center] < target:
        deep(ls[center + 1:], center + 1 + start)
    else:
        deep(ls[:center], start)


deep(nums, 0)
print(res)
