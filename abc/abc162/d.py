N = int(input())
S = input()
ans = S.count("R") * S.count("G") * S.count("B")

for i in range(N):
    for j in range(i + 1, N):
        if S[i] != S[j]:
            x = 2 * j - i
            if x < N and S[i] != S[x] and S[x] != S[j]:
                ans -= 1

print(ans)
