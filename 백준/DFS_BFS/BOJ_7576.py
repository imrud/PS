import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())        ## 가로(열), 세로(행)

graph = [list(map(int, input().split())) for _ in range(N)]     ## 상자 내 토마토 입력받기

## 오, 앞, 왼, 뒤 방향
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs():
    while que:
        x, y = que.popleft()    ## 다 익은 토마토의 위치 앞에서부터 꺼내기

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:     ## 인접 위치가 범위 내에 해당하고
                if graph[nx][ny] == 0:  ## 아직 익지 않은 토마토인 경우
                    graph[nx][ny] = graph[x][y] + 1  ## 인접 토마토가 익은 날짜는 기존 토마토보다 +1인 날짜
                    que.append((nx, ny))    ## 인접 토마토가 익었으니까 que에 삽입하기


que = deque()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:    ## 익은 토마토일 경우
            que.append((i, j))      ## 해당 위치를 que에 삽입

bfs()   ## 상자 내 익은 토마토 중심으로 인접 토마토 영향주기


flag = 1
res = -1

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:        ## bfs()했음에도 익지 않은 토마토 발견
            flag = 0
            print(-1)
            exit()

        res = max(res, graph[i][j])     ## 익은 날짜 최소 구하기

print(res-1)

# if flag == 0:
#     print(-1)
# elif res == 1:
#     print(0)
# else:
#     print(res-1)