K = int(input())
A, B = map(int, input().split())
ans = "NG"

if A % K == 0:
    ans = "OK"
elif (A // K + 1) * K <= B:
    ans = "OK"

print(ans)