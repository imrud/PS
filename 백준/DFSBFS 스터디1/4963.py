## 백준 : 4963
import sys
sys.setrecursionlimit(5000000)
input = sys.stdin.readline
# w : 너비(열), h : 높이(행)


def dfs(x, y):
    if 0 <= x < h and 0 <= y < w:
        if grid[x][y] == 1: ## 방문 확인
            grid[x][y] = 0
            
            dfs(x-1, y-1)
            dfs(x-1, y)
            dfs(x-1, y+1)
            dfs(x, y-1)
            dfs(x, y+1)
            dfs(x+1, y-1)
            dfs(x+1, y)
            dfs(x+1, y+1)
            return True
        
        return False
    


while True:
    w, h = map(int, input().split())

    ## 입력 마지막 판단
    if w == 0 and h == 0:
        break

    grid = []
    ## 지도 입력
    for _ in range(h):
        grid.append(list(map(int, input().split())))

    cnt = 0
    ## 땅의 판별
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1:     ## 땅이라면
                dfs(i, j)
                cnt += 1

    print(cnt)

    
