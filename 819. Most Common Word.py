class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        hold = []
        banned = set(banned)

        i = 0
        while i < len(paragraph):
            cur = ''
            if paragraph[i].isalpha():
                cur += paragraph[i]
                while i + 1 < len(paragraph) and paragraph[i + 1].isalpha():
                    cur += paragraph[i + 1]
                    i += 1
                hold.append(cur.lower())
            i += 1

        res = sorted(list(collections.Counter(hold).items()), key=lambda x: x[1], reverse=True)
        for i in range(len(res)):
            if res[i][0] not in banned:
                return res[i][0]
