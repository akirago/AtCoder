import numpy as np

N, K = map(int, input().split())

A = np.zeros(N, dtype=int)

for _ in range(K):
    input()
    for i in input().split():
        A[int(i) - 1] += 1

ans = 0
for i in A:
    if i == 0:
        ans += 1
print(ans)
