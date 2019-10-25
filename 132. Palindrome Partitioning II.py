class Solution:
    def candy(self, ratings: List[int]) -> int:

        lr = [1]
        n = len(ratings)
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                lr.append(lr[-1] + 1)
            else:
                lr.append(1)

        rl = [1]
        for j in range(n - 2, -1, -1):
            if ratings[j] > ratings[j + 1]:
                rl.insert(0, rl[0] + 1)
            else:
                rl.insert(0, 1)

        ans = 0
        for i in range(n):
            ans += max(lr[i], rl[i])

        return ans