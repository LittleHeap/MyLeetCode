def compress(chars):
    chars = list(chars)
    i = 0
    while i < len(chars):
        if i == 0:
            i += 1
        else:
            if isinstance(chars[i - 1], int):
                if chars[i] == chars[i - 2]:
                    chars[i - 1] = chars[i - 1] + 1
                    chars.pop(i)
                else:
                    i += 1
            else:
                if chars[i] == chars[i - 1]:
                    chars[i] = 2
                i += 1
    i = 0
    for i in range(len(chars)):
        if isinstance(chars[i], int):
            chars[i] = str(chars[i])

    return ''.join(chars)

print(compress('bbcceeee'))
print(compress('aaabbbcccaaa'))
print(compress('a'))