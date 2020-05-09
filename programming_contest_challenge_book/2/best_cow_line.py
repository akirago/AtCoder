N = 6
S = "ACDBCB"
T = ""
S_rev = S[::-1]

print(S_rev)
for _ in range(N):
    if S[0] < S_rev[0]:
        T += S[0]
        S = S[1:]
    else:
        T += S_rev[0]
        S_rev = S_rev[1:]

print(T)
