import bisect
low = 200
high = 405

three = [1]
five = [1]

pre = 1
while pre * 3 <= high:
    three.append(pre * 3)
    pre *= 3

pre = 1
while pre * 5 <= high:
    five.append(pre * 5)
    pre *= 5

print(three)
print(five)
res = 0

for num in three:
    start = bisect.bisect_left(five, low // num)
    end = bisect.bisect_left(five, high // num)
    #print(start, end)
    res += end - start

for num in five:
    start = bisect.bisect_left(three, low // num)
    end = bisect.bisect_left(three, high // num)
    print(start, end)
    res += end - start

print(res)