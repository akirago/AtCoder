import sys
N, M, K = map(int, input().split())

mod = 998244353

if N == 1:
    print(M)
    sys.exit()


t = M * (M - 1) ** (N - 1)
ans = t % mod
for i in range(K):
    t = t / (M - 1)
    t = t * (N - i - 1) / (1 + i)
    ans += t
    ans = ans % mod

print(ans)