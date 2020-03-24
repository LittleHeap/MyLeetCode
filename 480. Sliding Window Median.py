class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if k % 2 == 1:
            flag = 1
            index = k // 2
        else:
            flag = 0
            index1 = k // 2 - 1
            index2 = index1 + 1

        res = []
        hold = []

        for i in range(k - 1, len(nums)):
            if i == k - 1:
                for j in range(i + 1):
                    bisect.insort(hold, nums[j])
                if flag:
                    res.append(float(hold[index]))
                else:
                    res.append((hold[index1] + hold[index2]) / 2)
            else:
                r = bisect.bisect_left(hold, nums[i - k])
                hold.pop(r)
                bisect.insort(hold, nums[i])
                if flag:
                    res.append(float(hold[index]))
                else:
                    res.append((hold[index1] + hold[index2]) / 2)
        return res

