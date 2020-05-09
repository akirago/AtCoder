N = 6
S = "ACDBCB"
T = ""

for _ in range(6):
    if S[0] < S[-1]:
        S, p = S[1:], S[0]
        T = T + p
    else:
        S, p = S[:-1], S[-1]
        T = T + p

print(T)
