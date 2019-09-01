class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        big = word.lower()
        small = word.upper()
        if big == word or small == word:
            return True
        else:
            first = word[0].upper()
            back = word[1:].lower()
            if first + back == word:
                return True
            else:
                return False
