class Solution:
    def originalDigits(self, s: str) -> str:
        d = {}
        for i in range(97, 123):
            d[chr(i)] = 0

        for char in s:
            d[char] += 1

        res = []
        check_ls = [["z", 0], ["x", 6], ["w", 2], ["g", 8], ["h", 3], ["u", 4], ["o", 1], ["f", 5], ["s", 7], ["i", 9]]
        ls = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

        done = set()
        for ele in check_ls:
            t = d[ele[0]]
            for char in ls[ele[1]]:
                d[char] -= t
            for _ in range(t):
                heapq.heappush(res, ele[1])

        ans = ''
        while res:
            ans += str(heapq.heappop(res))

        return ans