ransomNote = 'aa'
magazine = 'ab'

d = {}

for ele in magazine:
    d[ele] = d.get(ele, 0) + 1

for ele in ransomNote:
    if d.get(ele) is None or d.get(ele) == 0:
        print(False)
        break
    else:
        d[ele] = d.get(ele) - 1

print(True)
