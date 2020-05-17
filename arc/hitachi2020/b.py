A, B, M = map(int, input().split())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
ans = 10000000
for _ in range(M):
    x, y, c = map(int, input().split())
    ans = min(ans, a[x - 1] + a[y - 1] - c)
a.sort()
b.sort()
print(min(ans, a[0] + b[0]))
