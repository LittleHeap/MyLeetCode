class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0

        citations.sort()
        citations.reverse()
        while citations and citations[-1] == 0:
            citations.pop()

        if not citations:
            return 0

        n = len(citations)
        for i in range(1, len(citations) + 1):
            if i == citations[i - 1]:
                return i
            elif i > citations[i - 1]:
                return i - 1
            elif i == n:
                return i