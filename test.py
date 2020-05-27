def compress(chars):
    if len(chars) < 2:
        return chars
    result = []
    count = 1
    pre_word = chars[0]
    for word in chars[1:]:
        if word != pre_word:
            if count == 1:
                result += pre_word
            else:
                result += (pre_word+str(count))
                count = 1
            pre_word = word
        else:
            count += 1
    if count != 1:  # compress the last letter
        result += (pre_word+str(count))
    else:
        result += pre_word
    return "".join(result)


print(compress('bbcceeee'))
print(compress('aaabbbcccaaa'))
print(compress('a'))
print(compress('peoqkerdddd'))
print(compress('testtttdd'))