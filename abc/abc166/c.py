import numpy as np

N, M = map(int, input().split())
H = [int(a) for a in input().split()]
good = np.zeros(N, dtype=int)
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if H[a] > H[b]:
        good[b] += 1
    elif H[a] < H[b]:
        good[a] += 1
    else:
        good[a] += 1
        good[b] += 1

ans = 0
for i in good:
    if i == 0:
        ans += 1
print(ans)
