class Solution:
    def accountsMerge(self, accounts):
        # create email to account dict to find related accounts
        d = defaultdict(list)

        for i, ele in enumerate(accounts):
            name = ele[0]
            email = ele[1:]
            for e in email:
                d[e].append(i)

        UF = [i for i in range(len(accounts))]


        def find(i):
            if i != UF[i]:
                UF[i] = find(UF[i])
            return UF[i]


        def union(a, b):
            UF[find(a)] = find(b)


        for v in d.values():
            if len(v) > 1:
                for i in range(len(v)):
                    union(v[0], v[i])

        resd = defaultdict(set)

        for i in range(len(accounts)):
            zu = find(i)
            resd[zu].update(set(accounts[i][1:]))

        res = []
        for ele in resd:
            res.append([accounts[ele][0]] + sorted(list(resd[ele])))

        return res