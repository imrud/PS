import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().split())     ## 가로(열), 세로(행), 높이

graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]     ## 3차원 배열 만들기

## 위, 아래, 왼쪽, 오른쪽, 앞, 뒤
dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

## deq에는 다 익은 토마토의 위치 삽입

def bfs():
    while deq:
        z, x, y = deq.popleft()   ## 높이가 먼저/ 다익은 토마토의 위치를 deq에서 꺼내기

        for i in range(6):      ## 총 여섯방향(위, 아래, 왼쪽, 오른쪽, 앞, 뒤)
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H: ## 범위 이내일 경우
                if graph[nz][nx][ny] == 0:  ## 방향 전환된 위치에서의 토마토가 안 익었을 경우
                    ## =1 처리가 아니라, +=1 해주는 이유는 -> 해당 위치의 값은 익기까지 걸린 날짜를 의미함
                    graph[nz][nx][ny] = graph[z][x][y] + 1      ## 해당 위치를 익은 토마토로 처리 해주기
                    deq.append([nz, nx, ny])    ## 전환된 토마토도 익었으니까 deq에 넣어주기

deq = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1:     ## 토마토가 다 익은 경우
                deq.append([i, j, k])

bfs()   ## 토마토 익히기

z = 1
result = -1

for i in graph:
    for j in i:
        for k in j:
            if k == 0:      ## 토마토가 안 익은 경우
                z = 0

            result = max(result, k)     ## 모든 토마토가 다 익기까지 걸린 시간 찾기 위해 max()로 비교해서 구하기


if z == 0:      ## 모두 익지 않은 경우
    print(-1)
elif result == 1:   ## 모두 익은 경우
    print(0)
else:
    print(result-1)
