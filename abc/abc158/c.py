import math

A, B = map(int, input().split())

ans = -1

a = math.floor(A * 12.5)
b = math.floor(B * 10)
if a <= b < a + 12:
    ans = b
elif b <= a < b + 10:
    ans = a
print(ans)
