s = 'ABBCZBAC'
s = list(s)

ans = 0
n = len(s)
remain = ['A', 'B', 'C']
index = []
for i in range(n):
    if s[i] in remain:
        index.append(i)
        remain.remove(s[i])

print(index)
# [0, 1, 3] 先找除ABC三个字母的索引，作为基础窗口

if len(index) != 3:
    print(0)
    # ABC都找不全就返回没有符合条件的子串

for i in range(n - 2):
    if len(index) != 3:
        # 后面没有满足条件窗口了，结束
        break
    if i <= index[0]:
        ans += n - index[-1]
        # 左索引还没触及窗口最前面的字母，保持窗口，这时子串从从i到窗口最后一个元素，以及后面的都满足
    else:
        temp = s[index[0]]
        # 左索引触及窗口最前面的字母了，更新窗口
        index.pop(0)
        # 删除窗口第一个元素索引
        for j in range(i, n):
            # 往后开始找删除的那个字母
            if s[j] == temp:
                index.append(j)
                # 找到后放在窗口里
                index.sort()
                # 给窗口内的索引排个序，保持顺序
                ans += n - index[-1]
                # 找到新的索引后，把这种情况当前满足的数量计入
                break
print(ans)
