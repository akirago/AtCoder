N = int(input())
ans = [0 for _ in range(N)]
A = [int(i) for i in input().split()]

for a in A:
    ans[a-1] += 1

for a in ans:
    print(a)
