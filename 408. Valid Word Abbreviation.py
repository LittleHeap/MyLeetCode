class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if len(word) == 0:
            return len(abbr) == 0

        stack = [word[0], '1']

        for i in range(1, len(word)):
            for k in range(len(stack)):
                if stack[k][-1].isdigit():
                    stack.append(stack[k][:-1] + str(int(stack[k][-1]) + 1))
                    stack[k] += word[i]
                else:
                    stack.append(stack[k] + word[i])
                    stack[k] += '1'

        return abbr in stack