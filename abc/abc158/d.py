S = input()
Q = int(input())
for _ in range(Q):
    T = list(input())
    T[0] = int(T[0])
    if T[0] == 1:
        S = S[::-1]
    else:
        T[2] = int(T[2])
        if T[2] == 1:
            S = T[4] + S
        else:
            S += T[4]
print(S)
