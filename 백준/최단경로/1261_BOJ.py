import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())        ## 가로크기 M(열), 세로크기 N(행)
arr = [list(input().strip()) for _ in range(N)]

dist = [[-1]*M for _ in range(N)]       ## 비용
dist[0][0] = 0  ##  출발 위치의 비용을 0으로 설정

que = deque()
que.append((0,0))   ## deque에 출발 위치 삽입

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs():
    while que:
        x, y = que.popleft()    ## 비용이 0인것부터 빼기(=비용이 작은것부터)

        for i in range(4):  ## 좌우상하 방향으로 설정
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:     ## 방향 전환한 위치가 arr의 범위 내에 있을 경우
                if dist[nx][ny] == -1:  ## 전환한 위치의 비용이 갱신되지 않은 경우
                    if arr[nx][ny] == '0':  ## 전환한 위치가 빈 방이라면
                        dist[nx][ny] = dist[x][y]   ## 전환한 위치의 가중치를 전환전 위치의 가중치로 설정
                        que.appendleft((nx, ny))    ## 전환한 위치는 deque에 appendleft()로 입력(가중치가 0이기 때문)
                    else:   ## 전환한 위치가 벽인 경우
                        dist[nx][ny] = dist[x][y] + 1   ## 전환한 위치의 비용 = 전환전 위치의 비용 + 1
                        que.append((nx, ny))    ## 전환한 위치의 비용은 0이 아니기 때문에 append()로 입력

bfs()   ## bfs 함수 실행하기
print(dist[N-1][M-1])   ## 결과 출력