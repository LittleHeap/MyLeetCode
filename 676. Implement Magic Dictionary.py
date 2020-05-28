class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = defaultdict(set)

    def buildDict(self, dict: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        for w in dict:
            self.d[len(w)].add(w)

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        for i in range(len(word)):
            for j in range(97, 123):
                if chr(j) != word[i] and word[:i] + chr(j) + word[i + 1:] in self.d[len(word)]:
                    return True
        return False

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)