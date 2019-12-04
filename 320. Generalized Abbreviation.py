word = "word"

n = len(word)

res = set()
res.add(word)
nums = [str(i) for i in range(1, 10)]
char = set()
for i in range(97, 123):
    char.add(str(chr(i)))


def deep(w):
    n = len(w)
    for i in range(n):
        for j in range(n):
            if i + j >= n or w[i + j] not in char:
                break
            if i == 0:
                if i + j + 1 < n and w[i + j + 1] in char:
                    new = [str(j + 1)]
                    new.extend(w[i + j + 1:])
                    res.add(''.join(new))
                    deep(new)
                if i + j + 1 == n:
                    new = [str(j + 1)]
                    res.add(''.join(new))
                    deep(new)
            elif w[i - 1] in char:
                if i + j + 1 < n and w[i + j + 1] in char:
                    new = w[:i]
                    new.append(str(j + 1))
                    new.extend(w[i + j + 1:])
                    res.add(''.join(new))
                    deep(new)
                if i + j + 1 == n:
                    new = w[:i]
                    new.append(str(j + 1))
                    res.add(''.join(new))
                    deep(new)

deep(list(word))
print(res)
print('11' in res)

