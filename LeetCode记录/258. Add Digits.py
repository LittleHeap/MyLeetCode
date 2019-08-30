num = 10

while num >= 10:
    num = list(str(num))
    new = 0
    for ele in num:
        new = new + int(ele)
    num = new
print(num)