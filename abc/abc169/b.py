N = int(input())
A = [int(a) for a in input().split()]
over = 10 ** 18
isOver = False
is0 = False
ans = 1
for a in A:
    ans *= a
    if ans > over:
        isOver = True
        ans = 1
    elif ans == 0:
        is0 = True
if is0:
    print(0)
elif isOver:
    print(-1)
else:
    print(ans)