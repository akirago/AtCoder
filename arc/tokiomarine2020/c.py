import sys
N, K = map(int, input().split())
if K > 42:
    print(" ".join(map(str, [N] * N)))
    sys.exit()
A = [int(i) for i in input().split()]
DP = [[0 for _ in range(N)] for _ in range(K+1)]
for i in range(N):
    DP[0][i] = A[i]

for i in range(1, K+1,1):
    B = [0] * N
    for j in range(N):
        pl, mi = min(j + DP[i-1][j], N-1), max(j - DP[i-1][j], 0)
        B[mi] += 1
        if pl + 1 < N:
            B[pl + 1] -= 1
    for j in range(1, N):
        B[j] += B[j-1]
    DP[i] = B
print(" ".join(map(str, DP[K])))
