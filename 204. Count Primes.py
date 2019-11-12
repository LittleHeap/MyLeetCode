class Solution:
    def countPrimes(self, n: int) -> int:
        hold = set()
        for i in range(2, n):
            hold.add(i)

        ans = 0
        for ele in list(hold):
            if ele in hold:
                ans += 1
                for d in range(ele, n + 1, ele):
                    if d in hold:
                        hold.remove(d)
        return ans