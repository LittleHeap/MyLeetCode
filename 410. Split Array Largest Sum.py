class Solution:
    def minAbbreviation(self, target: str, dictionary: List[str]) -> str:
        if not dictionary:
            return str(len(target))

        stack = ['1', target[0]]
        for i in range(1, len(target)):
            for j in range(len(list(stack))):
                if stack[j][-1].isdigit():
                    stack.append(stack[j] + target[i])
                    stack[j] = stack[j][:-1] + str(int(stack[j][-1]) + 1)
                else:
                    stack.append(stack[j] + '1')
                    stack[j] = stack[j] + target[i]

        hold = sorted(stack, key=lambda x: len(x))

        for ele in hold:
            flag = 1
            for p in dictionary:
                if len(p) != len(target):
                    continue
                ia = 0
                ib = 0
                t = 0
                while ia < len(ele):
                    temp = ia
                    if ele[ia].isdigit():
                        while ia + 1 < len(ele) and ele[ia + 1].isdigit():
                            ia += 1
                        l = int(ele[temp:ia + 1])
                        ib += l - 1
                    else:
                        if ele[ia] != p[ib]:
                            t = 1
                            break
                    ia += 1
                    ib += 1
                if t == 0:
                    flag = 0
                    break
            if flag == 1:
                return ele
        return hold[0]