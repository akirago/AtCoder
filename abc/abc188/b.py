_ = int(input())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))

total = 0
for i in range(len(X)):
    total += X[i] * Y[i]

if total == 0:
    print("Yes")
else :
    print("No")
