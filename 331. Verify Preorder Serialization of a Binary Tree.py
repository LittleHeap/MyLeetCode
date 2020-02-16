class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        preorder = preorder.split(',')

        stack = []

        for ele in preorder:
            if ele.isdigit():
                stack.append(ele)
            elif ele == '#':
                if len(stack) >= 3 and stack[-1] == '*' and stack[-2].isdigit():
                    stack.pop()
                    stack.pop()
                    stack.append('*')
                else:
                    stack.append('*')
            while len(stack) >= 3 and stack[-1] == '*' and stack[-2] == '*' and stack[-3].isdigit():
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append('*')

        if (len(stack) == 1 and stack[0] == '*') or not stack:
            return 1
        else:
            return 0