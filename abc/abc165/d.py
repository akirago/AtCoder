A, B, N = map(int, input().split())
ansNum = 0
if B > N:
    ansNum = N
else:
    ansNum = B - 1
print((A * ansNum // B - A * (ansNum // B)))
