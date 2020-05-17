K = int(input())
S = input()

if S.__len__() <= K:
    print(S)
else:
    print(S[0:K] + "...")
