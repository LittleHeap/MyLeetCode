class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hold = set()
        res = []
        for i in range(len(s) - 9):
            if s[i:i + 10] not in hold:
                hold.add(s[i:i + 10])
            elif s[i:i + 10] not in res:
                res.append(s[i:i + 10])
        return res
