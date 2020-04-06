class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:

        stackS = []
        stackT = []

        for ele in S:
            if ele == '#':
                if not stackS:
                    continue
                stackS.pop()
            else:
                stackS.append(ele)

        for ele in T:
            if ele == '#':
                if not stackT:
                    continue
                stackT.pop()
            else:
                stackT.append(ele)

        return stackS == stackT
