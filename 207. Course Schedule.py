class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        d = {}
        for i in range(numCourses):
            d[i] = []
        for ele in prerequisites:
            d[ele[0]].append(ele[1])

        flag = [0]
        fin = set()

        def deep(node):
            fin.add(node)
            if flag[0] == 1:
                return
            if node in done:
                flag[0] = 1
                return
            done.add(node)
            if d[node]:
                for pre in d[node]:
                    deep(pre)
            done.remove(node)

        for i in range(numCourses):
            done = set()
            if i not in fin:
                deep(i)
            if flag[0] == 1:
                break

        return flag[0] == 0