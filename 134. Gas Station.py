class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        pre = None
        for i in range(n):
            if i > 0 and gas[i] - cost[i] > 0 and gas[i - 1] - cost[i - 1] > 0:
                continue
            if gas[i] >= cost[i]:
                start = i
                cur = i
                fuel = gas[i]
                next = (i + 1) % n
                while next != i:
                    fuel -= cost[cur]
                    fuel += gas[next]
                    cur = next
                    if fuel < cost[cur]:
                        break
                    else:
                        next = (next + 1) % n
                if next == i:
                    return i
        return -1
