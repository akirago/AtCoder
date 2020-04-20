N, M = map(int, input().split())
A = [int(a) for a in input().split()]
asum = sum(A)
if N >= asum:
    print(N - asum)
else:
    print(-1)
