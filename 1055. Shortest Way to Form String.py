class Solution:
    def shortestWay(self, source: str, target: str) -> int:

        d = defaultdict(list)

        for i, char in enumerate(source):
            d[char].append(i)

        mark = []

        res = 0
        for i, char in enumerate(target):
            if not d[char]:
                return -1
            if i == 0:
                res += 1
                mark.append(d[char][0])
            else:
                index = bisect.bisect_right(d[char], mark[-1])
                if index == len(d[char]):
                    res += 1
                    mark.append(d[char][0])
                else:
                    mark.append(d[char][index])

        return res