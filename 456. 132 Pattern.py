import bisect

nums = [3, 1, 4, 2]

stack = []

for ele in nums:
    if not stack:
        stack.append(ele)
        continue

