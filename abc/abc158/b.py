N, A, B = map(int, input().split())

AB = A + B

ans = (N // AB) * A
rest = N % AB
if rest < A:
    ans += rest
else:
    ans += A
print(ans)

