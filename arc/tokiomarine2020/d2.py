import sys
N, K = map(int, input().split())
# A = [int(i) for i in input().split()]
A = [0] * N
DP = [[0 for _ in range(N)] for _ in range(K+1)]
for i in range(N):
    DP[0][i] = A[i]

for i in range(1, K+1,1):
    for j in range(N):
        pl, mi = min(j + DP[i-1][j], N-1), max(j - DP[i-1][j], 0)
        for k in range(mi, pl+1, 1):
            DP[i][k] += 1
    print(DP[i])
    if DP[i][0] == N & DP[i][N - 1] == N:
        print(" ".join(map(str, [N] * N)))
        sys.exit()

print(" ".join(map(str, DP[K])))
