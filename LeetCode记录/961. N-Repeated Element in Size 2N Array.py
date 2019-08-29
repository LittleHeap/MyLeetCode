A = [5, 1, 5, 2, 5, 3, 5, 4]

save = {}
for ele in A:
    save[ele] = save.get(ele, 0) + 1
    if save.get(ele) == 2:
        print(ele)
