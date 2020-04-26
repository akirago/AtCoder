A = 620
coins_val = [500, 100, 50, 10, 5, 1]
coins_num = [2, 0, 3, 1, 2, 3]


def solve(a):
    ans = 0
    for i in range(coins_val.__len__()):
        greed_num = a // coins_val[i]
        if greed_num >= coins_num[i]:
            a -= coins_val[i] * coins_num[i]
            ans += coins_num[i]
        else:
            a -= coins_val[i] * greed_num
            ans += greed_num
    return ans


print(solve(A))
