import itertools

N, M, X = map(int, input().split())
C = []
A = []
for i in range(N):
    x = [int(i) for i in input().split()]
    c, a = x[0], x[1:]
    C.append(c)
    A.append(a)
over = 1000000000
ans = over
for Z in itertools.product(range(0, 2), repeat=N):
    ctotal = 0
    atotal = [0] * M
    for i in range(N):
        if Z[i] == 1:
            ctotal += C[i]
            for j in range(A[i].__len__()):
                atotal[j] += A[i][j]
    ok = True
    for a in atotal:
        if a < X:
            ok = False
    if ok:
        ans = min(ans, ctotal)

if ans == over:
    print(-1)
else:
    print(ans)
