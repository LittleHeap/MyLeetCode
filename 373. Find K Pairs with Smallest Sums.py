import heapq

nums1 = [1, 2, 4]
nums2 = [-1, 1, 2]
k = 100

i1 = 0
i2 = 0
res = []
while 1:
    for j in range(i2, len(nums2)):
        heapq.heappush(res, [nums1[i1] + nums2[j], [nums1[i1], nums2[j]]])
    for i in range(i1 + 1, len(nums1)):
        heapq.heappush(res, [nums1[i] + nums2[i2], [nums1[i], nums2[i2]]])
    if i1 + 1 < len(nums1):
        i1 += 1
    if i2 + 1 < len(nums2):
        i2 += 1
    if len(res) >= k or (i1 == len(nums1) - 1 and i2 == len(nums2) - 1):
        break

ans = []
while len(ans) < k and res:
    ans.append(heapq.heappop(res)[1])

print(ans)