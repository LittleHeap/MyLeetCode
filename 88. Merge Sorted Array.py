nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
i1 = 0
i2 = 0
l = m + n
while 1:
    if m == 0:
        nums1[i1:i1 + m] = nums2[i2:i2 + n]
        break
    elif n == 0:
        break
    if nums1[i1] <= nums2[i2]:
        i1 += 1
        m -= 1
    else:
        nums1[i1 + 1:i1 + m + 1] = nums1[i1:i1 + m]
        nums1[i1] = nums2[i2]
        i1 += 1
        i2 += 1
        n -= 1

while len(nums1) > l:
    nums1.pop()
print(nums1)
