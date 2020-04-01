class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        line = []
        for ele in logs:
            ele = ele.split(':')
            line.append((int(ele[2]), ele[1], int(ele[0])))

        d = {}
        for i in range(n):
            d[i] = 0

        stack = []
        for time, mark, id in line:
            if not stack:
                stack.append([id, time])
            else:
                if mark == 'start':
                    if stack:
                        d[stack[-1][0]] += time - stack[-1][1]
                    stack.append([id, time])
                else:
                    last = stack.pop()
                    d[last[0]] += time - last[1] + 1
                    if stack:
                        stack[-1][1] = time + 1

        res = [0 for _ in range(n)]
        for ele in d:
            res[ele] = d[ele]

        return res