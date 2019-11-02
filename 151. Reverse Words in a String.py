class Solution:
    def reverseWords(self, s: str) -> str:
        hold = s.split(' ')

        hold.reverse()
        res = []
        for ele in hold:
            if ele != '':
                res.append(ele)

        ans = ''
        for ele in res:
            ans += ele + ' '

        ans = ans[:len(ans) - 1]
        return ans
