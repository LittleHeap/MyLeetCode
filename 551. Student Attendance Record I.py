class Solution:
    def checkRecord(self, s: str) -> bool:
        res = collections.Counter(s)

        if res.get('A', 0) <= 1 and s.find('LLL') == -1:
            return True
