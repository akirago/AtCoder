N = int(input())
A = [int(i) for i in input().split()]

total = int(N / 2)
dp = [[-1000000000 for _ in range(total)] for _ in range(N)]
print(dp)
dp[0][total - 1] = A[0]
dp[1][total - 1] = A[1]
dp[2][total - 1] = A[2]
for i in range(N):
    if i == 1 or i == 0:
        continue
    for jd in range(total - 1):
        j = total - 1 - jd
        dp[i][j - 1] += max(dp[i][j - 1], dp[i][j] + A[i])
        dp[i][j - 1] += max(dp[i][j - 1], dp[i][j] + A[i])
        print(i, j, dp[i][j])

print(max(dp[N - 1][0], dp[N - 2][0], dp[N - 3][0]))
