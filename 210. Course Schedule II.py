class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return [i for i in range(numCourses)]
        record = [[0, 0, i] for i in range(numCourses)]

        done = set()
        save = [[] for _ in range(numCourses)]
        for ele in prerequisites:
            save[ele[0]].append(ele[1])

        flag = [0]

        def deep(node):
            if flag[0] == 1 or node in done:
                return
            if node not in hold:
                hold.add(node)
            else:
                flag[0] = 1
                return
            record[node - 1][0] = start[0]
            start[0] += 1
            for pre in save[node - 1]:
                deep(pre + 1)
            record[node - 1][1] = start[0]
            start[0] += 1
            done.add(node)

        start = [1]
        for i in range(1, numCourses + 1):
            hold = set()
            if i not in done and flag[0] == 0:
                deep(i)
            done.add(i)

        if flag[0] == 0:
            res = sorted(record, key=lambda x: x[1])
            ans = []
            for ele in res:
                ans.append(ele[2])
            return ans
        else:
            return []
