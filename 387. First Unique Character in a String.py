class Solution:
    def firstUniqChar(self, s: str) -> int:
        hold = []
        appear = set()
        d = {}
        for i, ele in enumerate(list(s)):
            if ele not in appear:
                hold.append(ele)
                appear.add(ele)
                d[ele] = i
            elif ele in hold:
                hold.pop(hold.index(ele))

        if hold:
            return d[hold[0]]
        else:
            return -1