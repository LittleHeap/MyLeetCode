import copy

s1 = "hobobyrqd"
s2 = "hbyorqdbo"

ans = set()
q = list(s2)

def deep(s, p):
    if True in ans:
        return
    if len(s) == 2:
        s = list(s)
        s.sort()
        p = list(p)
        p.sort()
        if s == p:
            ans.add(True)
            return
        else:
            ans.add(False)
            return
    if len(s) == 1:
        if s == p:
            ans.add(True)
            return
        else:
            ans.add(False)
            return
    for index in range(1, len(s)):
        r = s[:index]
        l = s[index:]
        tr = list(r)
        tr.sort()
        tp = p[:index]
        tp = list(tp)
        tp.sort()
        if tr == tp:
            deep(r, p[:index])
            deep(l, p[index:])
        tp = p[-index:]
        tp = list(tp)
        tp.sort()
        if tr == tp:
            deep(r, p[-index:])
            deep(l, p[:-index])
    return

deep(s1,s2)

print(ans)
