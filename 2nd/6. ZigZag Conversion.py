s = "PAYPALISHIRING"
numRows = 4

save = [[] for _ in range(numRows)]
s = list(s)

index = 0
dir = 0
while s:
    save[index % numRows].append(s.pop(0))
    if dir == 0:
        index += 1
    else:
        index -= 1
    if index == numRows:
        index -= 2
        dir = 1
    if index == -1:
        index += 2
        dir = 0

print(save)
for i in range(1, numRows):
    save[0].extend(save[i])

print(''.join(save[0]))
