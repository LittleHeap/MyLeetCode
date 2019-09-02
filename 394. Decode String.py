s = "2[abc]3[cd]ef"

nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
stack = []

leftindex = []
for i, ele in enumerate(s):
    stack.append(ele)
    if ele == ']':
        stack.pop()
        curstr = []
        curnum = []
        while stack[-1] != '[':
            curstr.append(stack.pop())
        stack.pop()
        curstr.reverse()
        while stack and stack[-1] in nums:
            curnum.append(stack.pop())
        curnum.reverse()
        curnum = int(''.join(curnum))
        curstr = curstr * curnum
        stack.extend(curstr)

print(''.join(stack))



