class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:

        data = [[username[i], timestamp[i], website[i]] for i in range(len(username))]

        data.sort()

        dic = {}

        for u, t, w in data:
            if u not in dic:
                dic[u] = []
            dic[u].append(w)

        seq = {}

        for u, w in dic.items():
            if len(w) >= 3:
                for i in range(len(w) - 2):
                    for j in range(i + 1, len(w) - 1):
                        for k in range(j + 1, len(w)):
                            webs = (w[i], w[j], w[k])
                            if webs not in seq:
                                seq[webs] = set()
                            seq[webs].add(u)

        return sorted(seq.items(), key=lambda x: (-len(x[1]), x[0]))[0][0]