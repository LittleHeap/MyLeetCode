class Solution:
    def nextGreaterElement(self, n: int) -> int:

        n = list(str(n))

        cur = [n[-1]]
        for i in range(len(n) - 2, -1, -1):
            if max(cur) > n[i]:
                cur.append(n[i])
                cur.sort()
                index = bisect.bisect_right(cur, n[i])
                n[i] = cur[index]
                n = n[:i + 1] + cur[:index] + cur[index + 1:]
                if int(''.join(n)) <= 2 ** 31:
                    return int(''.join(n))
            else:
                cur.append(n[i])

        return -1
