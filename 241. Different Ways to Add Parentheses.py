class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:

        def deep(string):
            cur = []
            for i, c in enumerate(string):
                if c in '+-*':
                    for a in deep(string[:i]):
                        for b in deep(string[i + 1:]):
                            cur += [a + b if c == '+' else a - b if c == '-' else a * b]
            if not cur:
                return [int(string)]
            else:
                return cur

        return deep(input)