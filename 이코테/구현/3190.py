## [이코테_CH4] 백준: 3190-뱀
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())    ## 보드 크기
area = [[0]*n for _ in range(n)]

## 방향은 동, 남, 서, 북
directions = {0:(0, 1), 1:(1,0), 2:(0, -1), 3:(-1, 0)}
que = deque()       ## 지나가는 자리
time = deque()      ## 방향 정보(치고 빠지기 위해 deque로) 

k = int(input())    ## 사과 개수
for _ in range(k):
    a, b = map(int, input().split())
    area[a-1][b-1] = 1     ## 사과 표시

for _ in range(int(input())):
    x, c = map(str, input().split())
    time.append([int(x), c])


def Dummy():
    d = 0
    count = 0
    nx, ny = 0, 0       ## 시작위치
    que.append((nx, ny))        ## 현재 꼬리위치 que에 넣기
    area[nx][ny] = 4    ## 현재 위치 표시

    while True:
        count += 1
        nx = nx + directions[d][0]
        ny = ny + directions[d][1]

        if not 0 <= nx < n or not 0 <= ny < n:  ## 범위 벗어날 경우 
            break

        if area[nx][ny] == 1:   ## 사과가 있는 경우
            area[nx][ny] = 4    ## 방문 표시 & 꼬리 움직X
            que.append((nx, ny))

        elif area[nx][ny] == 0:
            area[nx][ny] = 4
            que.append((nx, ny))    ## 현재 꼬리 위치 추가
            dx, dy = que.popleft()
            area[dx][dy] = 0        ## 꼬리 표시를 0으로 바꾸기

        elif area[nx][ny] == 4:     ## 자기 몸일경우
            break

        if len(time) and time[0][0] == count:
            t, nd = time.popleft()      ## 시간, 방향 빼기
            if nd == 'L':
                d = (d+3) % 4
            elif nd == 'D':
                d = (d+1) % 4

    return count

        
            


print(Dummy())
            
            
