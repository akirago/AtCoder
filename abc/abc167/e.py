N, M, K = map(int, input().split())

dp = [[0] * (K + 2) for _ in range(N)]

x = 998244353
dp[0][0] = M
for j in range(1, N):
    for i in range(K + 1):
        dp[j][i + 1] += dp[j - 1][i] % x
        dp[j][i] += dp[j - 1][i] * (M - 1) % x
ans = 0
for i in range(K + 1):
    ans += dp[N - 1][i] % x
print(ans)