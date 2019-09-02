s = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M', 4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD',
     900: 'CM'}
n = [1, 5, 10, 50, 100, 500, 1000, 4, 9, 40, 90, 400, 900]
n.sort(reverse=True)
print(n)

num = 1994
i = 0
res = ''
while num != 0:
    if num >= n[i]:
        num -= n[i]
        res += s.get(n[i])
    else:
        i += 1

print(res)
