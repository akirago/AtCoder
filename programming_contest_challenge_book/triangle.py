n = int(input())
a = [int(n) for n in input().split()]
a.sort()
ans = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            print("i", a[i], "j", a[j], "k", a[k])
            if a[i] + a[j] > a[k]:
                ans = a[i] + a[j] + a[k]
print(ans)
