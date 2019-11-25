class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:

        str = str.split(' ')

        if len(str) != len(pattern):
            return False

        d = {}
        done = set()
        for i in range(len(pattern)):
            if pattern[i] in d:
                if str[i] != d[pattern[i]]:
                    return False
            else:
                if str[i] not in done:
                    d[pattern[i]] = str[i]
                    done.add(str[i])
                else:
                    return False
        return True