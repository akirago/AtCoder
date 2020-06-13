A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())
leng = abs(A - B)
move = V - W
if move <= 0:
    print("NO")
else:
    if move * T >= leng:
        print("YES")
    else:
        print("NO")