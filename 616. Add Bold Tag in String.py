class Solution:
    def addBoldTag(self, s: str, dict: List[str]) -> str:

        hold = []

        for word in dict:
            index = 0
            for i in range(len(s) - len(word) + 1):
                if s[i:i + len(word)] == word:
                    hold.append([i, i + len(word) - 1])

        i = 1
        hold.sort()
        while i < len(hold) and len(hold) > 1:
            if hold[i][0] >= hold[i - 1][0] and hold[i][0] <= hold[i - 1][1] + 1:
                hold[i - 1][1] = max(hold[i - 1][1], hold[i][1])
                hold.pop(i)
            else:
                i += 1
        # print(hold)
        i = 0
        stack = []
        while i < len(s):
            if hold and i == hold[0][0] and i == hold[0][1]:
                stack.append('<b>' + s[i] + '</b>')
                hold.pop(0)
            elif hold and i == hold[0][0]:
                stack.append('<b>')
                stack.append(s[i])
            elif hold and i == hold[0][1]:
                stack.append(s[i])
                stack.append('</b>')
                hold.pop(0)
            else:
                stack.append(s[i])
            i += 1
        return ''.join(stack)