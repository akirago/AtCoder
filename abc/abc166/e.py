N = int(input())
A = [int(i) for i in input().split()]
dp = [0] * 10 ** 7
ans = 0
for i in range(N):
    x = i + 1 - A[i]
    if x >= 0:
        ans += dp[x]
    y = i + 1 + A[i]
    if y < 10 ** 7:
        dp[y] += 1

print(ans)
