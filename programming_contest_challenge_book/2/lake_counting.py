n = int(input())
m = int(input())
lake = [["" for _ in range(n)] for _ in range(m)]
for i in range(m):
    s = input()
    for j in range(s.__len__()):
        lake[i][j] = s[j]

ans = 0

dxl = [-1, 0, 1]
dyl = [-1, 0, 1]


def dfs(x, y):
    lake[x][y] = "."
    for dx in dxl:
        for dy in dyl:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < m and 0 <= ny < n and not (x != nx and y != ny):
                if lake[nx][ny] == "W":
                    dfs(nx, ny)


for row in range(m):
    for column in range(n):
        if lake[row][column] == "W":
            ans += 1
            dfs(row, column)

print(ans)
