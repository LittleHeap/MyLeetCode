class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        def deep(string):
            val = 0
            d = collections.Counter(string)
            fei = set()
            for char, times in d.items():
                if times < k:
                    fei.add(char)
            if len(fei) == 0:
                return len(string)
            string = list(string)
            for i in range(len(string)):
                if string[i] in fei:
                    string[i] = '#'
            string = ''.join(string)
            cur = string.split('#')
            for ele in cur:
                if ele == '':
                    continue
                else:
                    val = max(val, deep(ele))
            return val

        return deep(s)