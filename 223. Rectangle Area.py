A = -3
B = 0
C = 3
D = 4
E = 0
F = -1
G = 9
H = 2

s = 0
s += (C - A) * (D - B)
s += (G - E) * (H - F)

if E <= C and E >= A and H <= D and H >= B:
    s -= (H - B) * (C - E)
elif G <= C and G >= A and H <= D and H >= B:
    s -= (H - B) * (C - E)
elif E <= C and E >= A and H <= D and H >= B:
    s -= (H - B) * (C - E)
elif E <= C and E >= A and H <= D and H >= B:
    s -= (H - B) * (C - E)
