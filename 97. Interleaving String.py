s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
s1 = list(s1)
s2 = list(s2)
s3 = list(s3)

i = 0
s1_index = []
for j in range(len(s3)):
    if i == len(s1):
        break
    if s1[i] == s3[j]:
        s1_index.append(j)
        i += 1

print(s1_index)



