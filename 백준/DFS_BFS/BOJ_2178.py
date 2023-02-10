import sys
from collections import deque

input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

## 너비 우선 탐색
## 포인트 : 따로 방문 확인 리스트, 가중치 리스트를 만들지 않고 'graph[x][y] == 1'로 갈 수 있는지의 여부 + 가중치를 한 번에 판단한다.
def bfs(x, y):
    que = deque()   ## deque 생성
    que.append((x,y))

    while que:  ## 큐가 빌 때까지 반복
        x, y = que.popleft()    ## 맨 앞의 원소 꺼내기

        ## 현재 위치에서 4가지 방향으로 전환
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            ## 전환 좌표값이 범위 내 값이고 이동할 수 있는 칸 일때
            if (0 <= nx < N and 0 <= ny < M) and (graph[nx][ny] == 1):
                que.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1     ## 전환된 위치의 이동거리 = 이전 값 +1


N, M = map(int, input().split())    ## 행, 열

graph = []      ## 미로 입력받을 리스트 선언

for _ in range(N):      ##  미로 입력받기
    graph.append(list(map(int, input().rstrip())))

bfs(0, 0)   ## 출발

print(graph[N-1][M-1])
