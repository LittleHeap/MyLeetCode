class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        d = {}
        for i in range(n):
            d[i] = []

        for ele in edges:
            d[ele[0]].append(ele[1])
            d[ele[1]].append(ele[0])

        fin = set()

        flag = [0]
        def deep(node, pre):
            if node in done:
                flag[0] = 1
                return
            else:
                done.add(node)
                fin.add(node)
                for next in d[node]:
                    if next != pre:
                        deep(next, node)


        for i in range(n):
            if i > 0 and i not in fin:
                return False
            if i not in fin:
                done = set()
                deep(i, -1)
            if flag[0] == 1:
                return False
        return True

