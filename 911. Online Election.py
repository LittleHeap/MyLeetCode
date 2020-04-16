class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.seek = []
        d = defaultdict(int)

        head = -1
        d[head] = -1

        for i, ele in enumerate(persons):
            d[ele] += 1
            if d[ele] >= d[head]:
                head = ele
            self.seek.append(head)

    def q(self, t: int) -> int:
        index = bisect.bisect_left(self.times, t + 1)
        return self.seek[index - 1]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)