import bisect
n = int(input())
m = int(input())
kl = [int(i) for i in input().split()]
kl.sort()
kk = set()
for x in kl:
    for y in kl:
        kk.add(x+y)
ans = "No"
for i in range(n):
    for j in range(i, n):
        for x in kk:
            if x == 9 - kl[i] - kl[j]:
                print(i, j)
                break
print(ans)
