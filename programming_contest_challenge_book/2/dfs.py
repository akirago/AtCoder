n = int(input())
a = [int(n) for n in input().split()]
k = int(input())


def dfs(i, summary):
    if i == n:
        return summary == k
    if dfs(i + 1, summary):
        return True
    if dfs(i + 1, summary + a[i]):
        return True
    return False


print(dfs(0, 0))
