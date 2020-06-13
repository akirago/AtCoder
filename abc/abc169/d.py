N = int(input())
ans = 0
for i in range(2, 10 ** 6 + 1):
    for x in range(1, 40):
        y = i ** x
        if N // y == N / y:
            ans += 1
            N = N // y
        else:
            while N // i == N / i:
                N = N // i
            break


if N > 10 ** 6:
    ans += 1
print(ans)