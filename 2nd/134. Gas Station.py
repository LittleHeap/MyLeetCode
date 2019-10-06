class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        def can(index):
            origin = index
            remain = 0
            while index != (origin - 1) % n:
                remain += gas[index]
                remain -= cost[index]
                if remain < 0:
                    return False
                else:
                    index += 1
                    index %= n
            if index != (origin - 1) % n:
                return False
            elif remain + gas[index] - cost[index] < 0:
                return False
            else:
                return True

        start = 0
        res = -1
        hold = set()
        while 1:
            if start == n:
                break
            while start < n and gas[start] < cost[start]:
                start += 1
            if start == n:
                break
            hold.add(start)
            if start - 1 not in hold and can(start):
                res = start
                break
            else:
                start += 1
        return res