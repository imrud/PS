## 백준 2468번 : 안전 영역
import sys
sys.setrecursionlimit(10**6) # 재귀의 깊이 변경 (RecursionError)
input = sys.stdin.readline

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

def dfs(x, y, z):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if grid[x][y] > z and check[x][y] == 0:

        ## 방문 표시하기
        check[x][y] = 1

        ## 근처에 영역 탐색하기
        dfs(x-1, y, z)
        dfs(x+1, y, z)
        dfs(x, y-1, z)
        dfs(x, y+1, z)

        return True
    return False
        

#print(grid)
#maxN = max(map(max, grid))
#minN = min(mapgr(min, grid))


##area = []
mm = 0
#for h in range(1, maxN+1):
for h in range(max(map(max, grid))):
    ## 높이 변할때마다 안전 영역 개수, 방문 표시 리스트 초기화
    cnt = 0
    check = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] > h and check[i][j] == 0:
                cnt += 1
                dfs(i, j, h)
               
    mm = max(cnt, mm)
    #print(cnt, mm)

print(mm)
                

                
                
