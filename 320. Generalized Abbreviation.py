word = 'abcdefghijklmn'

stack = [word[0], '1']
i = 1
while i < len(word):
    print(stack)
    newstack = []
    for ele in stack:
        if ele[-1].isdigit():
            newstack.append(ele + word[i])
            newstack.append(ele[:-1] + str(int(ele[-1]) + 1))
        else:
            newstack.append(ele + word[i])
            newstack.append(ele + '1')
    i += 1
    stack = newstack


print(stack)