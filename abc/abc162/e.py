N, K = map(int, input().split())
mod = 10 ** 9 + 7
ans = 0
dp = [0] * (K + 10)

for i in range(K, 0, -1):
    x = K // i
    a = pow(x, N, mod)
    cnt = 2
    while i * cnt <= K:
        a -= dp[i * cnt]
        cnt += 1
    a %= mod
    dp[i] = a
    ans += a * i
    ans %= mod
print(ans)
