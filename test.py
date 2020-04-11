prefixes = list('+1**23/14')

d = ['/', '*', '+', '-']


for cur in d:
    stack = []
    for char in prefixes:
        stack.append(char)
        while stack and len(stack) >= 3 and stack[-3] == cur and (stack[-2].isdigit() or len(stack[-2]) > 1):
            temp1 = stack.pop()
            temp2 = stack.pop()
            stack.pop()
            stack.append(temp2 + cur + temp1)
        #print(stack)
    prefixes = stack

print(prefixes)

infix = list(prefixes[0])

for cur in d:
    stack = []
    for char in infix:
        stack.append(char)
        if stack and len(stack) >= 3 and stack[-2] == cur and (stack[-3].isdigit() or len(stack[-3]) > 1):
            temp1 = stack.pop()
            stack.pop()
            temp2 = stack.pop()
            stack.append(temp2 + temp1 + cur)
        print(stack)
    infix = stack

print(infix)

