class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        d = {}

        for i in range(n):
            d[i] = []

        for ele in edges:
            d[ele[0]].append(ele[1])
            d[ele[1]].append(ele[0])


        def deep(node):
            if node in done:
                return
            else:
                done.add(node)
                for ele in d[node]:
                    deep(ele)


        done = set()
        ans = 0
        for i in range(n):
            if i not in done:
                deep(i)
                ans += 1
        return ans