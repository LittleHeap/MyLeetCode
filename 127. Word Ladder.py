class Solution:
    def ladderLength(self, begin: str, end: str, w: List[str]) -> int:

        w = set(w)

        q = [begin]
        done = set()
        done.add(begin)
        chars = list('abcdefghijklmnopqrstuvwxyz')

        step = 1
        while q:
            step += 1
            newq = []
            for word in q:
                for i in range(len(word)):
                    for char in chars:
                        if char != word[i]:
                            new = word[:i] + char + word[i + 1:]
                            if new in w and new == end:
                                return step
                            elif new not in done and new in w:
                                newq.append(new)
                                done.add(new)
            q = newq
        return 0
