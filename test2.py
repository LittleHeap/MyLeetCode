instances = 1
averageUtil = [5, 10 ,80]


index = 0
n = len(averageUtil)
up = 200000000
while index < n:
    if averageUtil[index] > 60:
        if instances <= up // 2:
            instances *= 2
            index += 10
            continue
    elif averageUtil[index] < 25:
        if instances > 1:
            instances = (instances + 1) // 2
            index += 10
            continue
    index += 1

print(instances)