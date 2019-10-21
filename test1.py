s = '06:34'

s = s.split(':')
h = list(s[0])
m = list(s[1])

if h[0] == '?':
    h[0] = '2'
if h[1] == '?':
    if int(h[0]) <= 1:
        h[1] = '9'
    else:
        h[1] = '3'

if m[0] == '?':
    m[0] = '5'
if m[1] == '?':
    m[1] = '9'

print(''.join(h) + ':' + ''.join(m))
