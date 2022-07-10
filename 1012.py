#1012: 유기농 배추
import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    ## 더 이상 배추밭이 아닌 경우
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if field[x][y] == 1:    ## 배추 심어졌다면

        ## 방문 확인 표시
        field[x][y] = -1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)

        return True
    return False


t = int(input())

for _ in range(t):
    m, n, k = map(int,input().split())      ## m:가로길이(열), n:세로 길이(행)
    field = [[0]*m for _ in range(n)]

    ## 배추밭 행렬
    for _ in range(k):
        p, q = map(int, input().split())
        field[q][p] = 1

    count = 0 ## 배추지렁이 개수
    for i in range(m):
        for j in range(n):
            if field[j][i] == 1:    ## 배추 심어진 경
                dfs(j,i)

                #카운트 1 증가
                count += 1

    print(count)
