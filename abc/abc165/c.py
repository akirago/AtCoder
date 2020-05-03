import numpy as np
import itertools

N, M, Q = map(int, input().split())
a = np.zeros(Q, dtype=int)
b = np.zeros(Q, dtype=int)
c = np.zeros(Q, dtype=int)
d = np.zeros(Q, dtype=int)
for i in range(Q):
    a[i], b[i], c[i], d[i] = map(int, input().split())
ans = 0
for A in itertools.combinations_with_replacement(range(1, M+1), N):
    tmp = 0
    for i in range(Q):
        if A[b[i]-1] - A[a[i]-1] == c[i]:
            tmp += d[i]
    ans = max(ans, tmp)

print(ans)
