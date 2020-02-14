class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        e = {}
        res = {}

        if not edges:
            return [0]

        for ele in edges:
            if ele[0] not in e:
                e[ele[0]] = []
            if ele[1] not in e:
                e[ele[1]] = []
            e[ele[0]].append(ele[1])
            e[ele[1]].append(ele[0])

        start = []
        for ele in e.keys():
            if len(e[ele]) == 1:
                start.append(ele)

        n = [0]
        res = [0]

        def deep(node, line, done):
            done.add(node)
            child = e[node]
            if len(child) == 1 and child[0] in done:
                if len(line) > n[0]:
                    n[0] = len(line)
                    res[0] = line.copy()
                return
            else:
                for new in child:
                    if new not in done:
                        line.append(new)
                        deep(new, line, done)
                        line.pop()

        for ele in start:
            l = [ele]
            s = set()
            s.add(ele)
            deep(ele, l, s)

        if len(res[0]) % 2 == 1:
            return [res[0][(len(res[0]) - 1) // 2]]
        else:
            return [res[0][(len(res[0]) - 1) // 2], res[0][(len(res[0]) - 1) // 2 + 1]]