N = int(input())
ans = 0
for i in range(N):
    i = i + 1
    if i % 3 != 0 and i % 5 != 0:
        ans += i

print(ans)
