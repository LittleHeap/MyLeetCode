nums = [8,10,2]

for ele in nums:
    print(bin(ele))

m = max(nums)
m = str(bin(m)[2:])

s = ''
for char in m:
    if char == '0':
        s += '1'
    else:
        s += '0'

s = int(s, 2)
m = int(m, 2)
print(s)
print(m)

temp = float('inf')
another = 0
for ele in nums:
    print(ele)
    if ele != m and abs(ele - s) < temp:
        temp = abs(ele - s)
        another = ele

print(another)
print(another ^ m)
