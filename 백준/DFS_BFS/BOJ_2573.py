import sys
from copy import deepcopy
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())    ## 행, 열
area = [list(map(int, input().split())) for _ in range(N)]



def bfs(sx, sy):
    que = deque()
    que.append((sx, sy))
    visited[sx][sy] = 1      ## 현재 위치 방문 처리하기
    seaList = []    ## 현재 위치에서 인접한 바다 위치 저장하기 위한 리스트

    while que:
        x, y = que.popleft()
        sea = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<M:
                if area[nx][ny] == 0:       ## 인접한 위치가 바닷물인 경우
                    sea += 1        ## 바다 개수 증가
                elif area[nx][ny] and visited[nx][ny] == 0:  ## 인접한 위치가 빙산, 아직 방문 전
                    que.append((nx, ny))
                    visited[nx][ny] = 1    ## 방문 확인 처리

        if sea > 0:
            seaList.append((x, y, sea))   ## 인접 바다가 있을 경우, 현재 위치와 인접한 바다의 개수 추가

    for x, y, sea in seaList:
        area[x][y] = max(0, area[x][y] - sea)

    return 1

iceberg = []    ## 빙산 위치 담을 리스트
for i in range(N):
    for j in range(M):
        if area[i][j] != 0:
            iceberg.append((i, j))  ## 빙산 위치를 추가하기

year = 0    ## 빙산이 2개로 분리되는 년도
while iceberg:
    visited = [[0]*M for _ in range(N)]     ## 방문 확인 리스트
    delIce = []     ## 바닷물로 녹아버린 빙산 위치 담을 리스트
    group = 0   ## 덩어리 개수

    for i, j in iceberg:
        if area[i][j] != 0 and visited[i][j] == 0:       ## 현재 위치가 빙산, 방문 전
            group += bfs(i, j)
        if area[i][j] == 0:     ## 현재 위치가 빙산에서 바닷물로 다 녹아버린 경우 -> delIce에 추가
            delIce.append((i,j))
    if group > 1:       ## 빙산이 2개로 분리된 경우
        print(year)
        break

    iceberg = list(set(iceberg) - set(delIce))      ## 빙산 업데이트(현재 빙산에서 녹은 빙산 위치 빼기)
    year += 1   ## 횟수 증가

if group < 2:   ## 위의 while문 끝날때까지 빙산 분리가 안 이루어진 경우
    print(0)


## pypy로 실행했을 경우 통과
# ## 빙산 다 녹았는지 확인하는 함수
# def check_sea():
#     for i in range(N):
#         for j in range(M):
#             if area[i][j] != 0:     ## 해당 위치가 빙산일 경우(바닷물X)
#                 return False
#     return True
#
# ## 빙산 주변의 바닷물(0) 개수 확인하는 함수
# def count_around(x, y):
#     cnt = 0
#
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#
#         if 0 <= nx < N and 0 <= ny < M and area[nx][ny] == 0:  ## 범위 내 존재, 해당 위치가 바닷물인 경우
#             cnt += 1
#     return cnt
#
# def bfs(x, y):
#     que = deque()
#     que.append((x, y))    ## 현재 빙산의 위치를 que에 삽입
#     visited = [[False]*M for _ in range(N)]     ## 방문 확인 리스트 생성
#     visited[x][y] = True    ## 현재 위치 방문 확인
#
#     while que:
#         x, y = que.popleft()    ## 첫 번째 요소 꺼내기
#
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             if 0<=nx<N and 0<=ny<M and visited[nx][ny]==False and tmp_area[nx][ny]!=0: ## 범위 내 존재, 현재 위치 방문 전, 빙산인 경우
#                 visited[nx][ny] = True  ## 방문 확인
#                 tmp_area[nx][ny] = 0        ## 연결 된 빙산은 0으로 처리하기
#                 que.append((nx, ny))
#
#
# year = 0
# ## 모든 빙산이 녹을때까지 반복
# while True:
#     year += 1
#
#     if check_sea():     ## True 반환 -> 빙산 존재하지 않고 모두 바닷물인경우
#         print(0)
#         break       ## while문 빠져나가기
#
#     tmp_area = [[0]*M for _ in range(N)]
#     for i in range(N):
#         for j in range(M):
#             if area[i][j] != 0:     ## 현재 위치가 빙산이라면
#                 sCnt = count_around(i, j)        ## 동,서,남,북 방향 바닷물 개수 확인
#                 iCnt = area[i][j] - sCnt    ## 바닷물의 수만큼 녹은 빙산의 높이
#
#
#                 ## 변경된 값은 바로 area에 반영하지 않고 tmp에 반영
#                 tmp_area[i][j] = iCnt if iCnt >= 0 else 0
#                 # if iCnt >= 0:    ## 빙산의 높이가 0이상 -> iCnt 값 그대로
#                 #     tmp_area[i][j] = iCnt
#                 # else:
#                 #     tmp_area[i][j] = 0
#     area = deepcopy(tmp_area)
#
#     cnt = 0
#     for i in range(N):
#         for j in range(M):
#             if tmp_area[i][j] != 0:     ## 이번년도에서 녹은 빙산에서 땅덩어리 체크
#                 bfs(i, j)
#                 cnt += 1
#
#     if cnt >= 2:        ## 덩어리가 2개 이상일경우
#         print(year)
#         break
