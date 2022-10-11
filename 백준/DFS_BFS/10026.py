## 백준 10026: 적록색약
import sys
sys.setrecursionlimit(10 ** 6)


def dfs(x, y, z):
    if (0 <= x < n) and (0 <= y < n):
        if visited[x][y] == 0 and grid[x][y] == z:
            visited[x][y] = 1
            dfs(x-1, y, z)
            dfs(x+1, y, z)
            dfs(x, y-1, z)
            dfs(x, y+1, z)
        

n = int(sys.stdin.readline())
grid = [list(map(str, sys.stdin.readline().strip())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]     ## 색칠 확인

## 색약X
cnt1 = 0   
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:      ## 방문
            cnt1 += 1
            dfs(i, j, grid[i][j])

## R->G 변환
for i in range(n):
    for j in range(n):
        if grid[i][j] == "R":
            grid[i][j] = "G"           
                        
## 색약O
cnt2 = 0
visited = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            cnt2 += 1
            dfs(i, j, grid[i][j])

print(cnt1, cnt2)
