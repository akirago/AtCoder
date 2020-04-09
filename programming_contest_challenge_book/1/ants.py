L = int(input())
n = int(input())
x = [int(n) for n in input().split()]
x.sort()
ans_min = 0
ans_max = max(abs(L - x[0]), abs(L - x[n-1]))
for i in x:
    ans_min = max(ans_min, min(i, L - i))
print(ans_min)
print(ans_max)