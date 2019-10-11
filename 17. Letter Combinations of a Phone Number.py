class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        save = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'],
                7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}

        res = []
        n = len(digits)
        if n == 0:
            return []

        def deep(index, cur):
            if index == n:
                res.append(cur)
                return
            hold = save[int(digits[index])]
            for ele in hold:
                newcur = copy.deepcopy(cur)
                newcur += ele
                deep(index + 1, newcur)

        deep(0, '')
        return res