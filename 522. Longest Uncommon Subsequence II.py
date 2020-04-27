class Solution:
    def findLUSlength(self, strs: List[str]) -> int:

        def submatch(a, b):
            i = -1
            for char in b:
                i = a.find(char, i + 1)
                if i < 0:
                    return False
            return True

        d = collections.Counter(strs)

        temp = sorted(d.items(), key=lambda x: len(x[0]), reverse=True)

        for i, (word, times) in enumerate(temp):
            if times == 1:
                flag = 1
                for j in range(i - 1, -1, -1):
                    if submatch(temp[j][0], word):
                        flag = 0
                        break
                if flag:
                    return len(word)

        return -1