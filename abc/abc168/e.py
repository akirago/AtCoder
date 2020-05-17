N = int(input())
bad = 1
X = {}
Y = {}

for _ in range(N):
    a, b = map(int, input().split())
    if (a >= 0 and b >= 0) or (a < 0 and b < 0):
        a = abs(a)
        b = abs(b)

        test = str(a / b)
        testa = str(b / a)
        if test in X:
            X[test] += 1
        else:
            X[test] = 1
        if testa in Y:
            bad = bad * (Y[testa] + 1) / (Y[testa] + 2) * 2
    else:
        a = abs(a)
        b = abs(b)
        test = str(a / b)
        testa = str(b / a)
        if test in Y:
            Y[test] += 1
        else:
            Y[test] = 1
        if testa in X:
            bad = bad * (X[testa] + 1) / (X[testa] + 2) * 2
print(int((2 ** N / bad - 1) % 1000000007))
