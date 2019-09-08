s = ")()())"

left = 0
right = len(s) - 1
while s[left] == ')':
    left += 1
while s[right] == '(':
    right -= 1
s = s[left: right + 1]
print(s)

ans = 0
l = 0
r = 0
first = 0
cursor = 0
n = len(s)
while 1:
    if cursor == n:
        if first == n - 1 or first == n:
            break
        else:
            first += 1
            cursor = first
            l = 0
            r = 0
    print([first, cursor])
    if s[cursor] == '(':
        l += 1
        cursor += 1
    else:
        r += 1
        cursor += 1
    if r > l:
        first = cursor
        l = 0
        r = 0
    elif r == l:
        ans = max(ans, cursor - first)

print(ans)
