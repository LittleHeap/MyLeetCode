class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return ''.join('%d:' % len(s) + s for s in strs)

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        while s:
            index = s.index(':')
            l = int(s[:index])
            res.append(s[index + 1:index + l + 1])
            s = s[index + l + 1:]

        return res

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))