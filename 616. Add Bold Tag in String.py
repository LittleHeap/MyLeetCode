class Solution:
    def addBoldTag(self, s: str, dict: List[str]) -> str:

        hold = []

        for word in dict:
            index = 0
            while s.find(word, index) != -1:
                cur = s.find(word, index)
                hold.append([cur, cur + len(word) - 1])
                index = cur + 1

        # print(hold)
        hold.sort()

        i = 1
        while i < len(hold) and len(hold) > 1:
            if hold[i][0] >= hold[i - 1][0] and hold[i][0] <= hold[i - 1][1] + 1:
                hold[i - 1][1] = max(hold[i - 1][1], hold[i][1])
                hold.pop(i)
            else:
                i += 1

        i = 0
        index = 0
        stack = []
        while i < len(s):
            if index < len(hold) and i == hold[index][0] and i == hold[index][1]:
                stack.append('<b>' + s[i] + '</b>')
                index += 1
            elif index < len(hold) and i == hold[index][0]:
                stack.append('<b>')
                stack.append(s[i])
            elif index < len(hold) and i == hold[index][1]:
                stack.append(s[i])
                stack.append('</b>')
                index += 1
            else:
                stack.append(s[i])
            i += 1
        return ''.join(stack)