# 백준 1743: 음식물 피하기
import sys
sys.setrecursionlimit(10**6) # 재귀의 깊이 변경 (RecursionError)


def dfs(x, y):
    global cur
    
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if grid[x][y] == 1:
        cur += 1
        grid[x][y] = 0
        
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)

        return True
    return False


n, m, k = map(int, sys.stdin.readline().split(' '))
grid = [[0]*m for _ in range(n)]

for _ in range(k):
    r, c = map(int, sys.stdin.readline().split(' '))
    grid[r-1][c-1] = 1



maxN = 0
cur = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
##            dfs(i, j)
##            maxN = max(cur, maxN)
            
            if cur >= maxN:
                maxN = cur
            cur = 0

print(maxN)
            
            
            
