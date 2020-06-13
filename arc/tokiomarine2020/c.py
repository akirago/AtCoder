import sys
N, K = map(int, input().split())
if N < 2 ** K - 1:
    print(" ".join(map(str, [N] * N)))
    sys.exit()
A = [int(i) for i in input().split()]
DP = [[0 for _ in range(N)] for _ in range(K+1)]
for i in range(N):
    DP[0][i] = A[i]

for i in range(1, K+1,1):
    B = [0] * N
    for j in range(N):
        if DP[i-1][j] == 0: continue
        pl, mi = min(j + DP[i-1][j], N-2), max(j - DP[i-1][j], 0)
        B[mi] += 1
        B[pl + 1] -= 1
        print(j, B)
    print(B)
    for j in range(1, N):
        B[j] += B[j-1]
    for j in range(N):
        B[j] += 1
    DP[i] = B
print(" ".join(map(str, DP[K])))
