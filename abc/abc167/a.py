S = input()
T = input()
if S.__len__() + 1 == T.__len__() and S == T[:S.__len__()]:
    print("Yes")
else:
    print("No")
