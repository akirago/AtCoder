import sys
N = int(input())
A = [int(a) for a in map(int, input().split())]
root = [1 - A[0]]
for i in range(1, A.__len__()):
    r = root[i-1] * 2 - A[i]
    if r > 0:
        root.append(r)
    elif r == 0 and i == N:
        root.append(r)
    else:
        print(-1)
        sys.exit()
print(root)
ans = 0
for a in A:
    ans += a
now = 0
for i in range(A.__len__() - 1, -1, -1):
    print(i)
    now += A[i]
    ans += min(root[i], now)

print(ans)