class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:

        index = [0 for _ in range(len(primes))]

        res = [1]
        cur = [1]

        d = defaultdict(list)

        for i in range(1, n + 1):
            mini = heapq.heappop(cur)
            if mini == 1:
                for j, k in enumerate(index):
                    heapq.heappush(cur, mini * primes[j])
                    d[mini * primes[j]].append(j)
            else:
                res.append(mini)
                for j in d[mini]:
                    index[j] += 1
                    if res[index[j]] * primes[j] not in cur:
                        heapq.heappush(cur, res[index[j]] * primes[j])
                    d[res[index[j]] * primes[j]].append(j)
                del d[mini]

        return res[-1]