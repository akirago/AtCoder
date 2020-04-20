mod = 10 ** 9 + 7
N, K = map(int, input().split())

ans = 0

lst = [int(i) for i in range(N + 1)]
internal = 1
for i in range(N + 1):
    internal += lst[N - i] - lst[i]
    if i + 1 >= K:
        ans += internal
        ans = ans % mod

print(ans)
