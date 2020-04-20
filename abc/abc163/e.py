N = int(input())
A = [int(i) for i in input().split()]
s = 0
AP = []
for a in A:
    s += 1
    AP.append((a, s))

AP.sort()

lst = [int(i) for i in range(1, N + 1)]
ans = 0
dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == 0:
            dp[j][j][i] = AP[i][0] * abs(AP[i][1] - j)
        else:
            if j - i >= 0:
                dp[j - i][j][i] = dp[j - i + 1][j][i - 1] + AP[i][0] * abs(AP[i][1] - (j - i))
            if j + i < N:
                dp[j + i][j][i] = dp[j - i + 1][j][i - 1] + AP[i][0] * abs(AP[i][1] - (j + i))
for i in range(N):
    ans = max(ans, dp[0][N-1][i])
print(ans)
