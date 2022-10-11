## 백준 2583번: 영역 구하기
import sys
sys.setrecursionlimit(10**6) # 재귀의 깊이 변경 (RecursionError)

## dfs 함수
def dfs(x, y):
    global cnt
    
    if x < 0 or x >= m or y < 0 or y >= n:    ## 범위 확인
        return False

    if grid[x][y] == 0:
        cnt += 1

        ## 방문확인
        grid[x][y] = 1

        ## 근처에 영역 탐색하기
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)

        return True
    return False

    


## 입력 받기
m, n, k = map(int, sys.stdin.readline().split(' '))
grid = [[0]*n for _ in range(m)]  

## 모눈 종이에 표시하기
for _ in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split(' '))
    ## x -> 열(가로), y -> 행(세로)
    for i in range(y1, y2):
        for j in range(x1, x2):
            #grid[i][j].append(1)
            grid[i][j] = 1


#count = 0
cnt = 0
area = []
## 영역 구하러 가기
for i in range(m):
    for j in range(n):
        if grid[i][j] == 0:
            dfs(i, j)

            #count += 1      ## 영역 총 개수
            area.append(cnt)
            cnt = 0

#print(count)
print(len(area))
area.sort()
for i in area:
    print(i, end=' ') 
    
    
