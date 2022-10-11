## [CH4] 실전문제 - 게임개발
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
x, y, d = map(int, input().split())

## 방문 위 저장 리스트 0으로 초기화
visited = [[0]*m for _ in range(n)]

## 현재 좌표 방문 처리
visited[x][y] = 1


## 전체 맵정보 입력
grid =[]
for _ in range(n):
    grid.append(list(map(int, input().split())))


## 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

## 왼쪽의로 회전
def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

count = 1
turn_time = 0

while True:
    # 1. 왼쪽 회전
    turn_left()
    nx = x + dx[d]
    ny = y + dy[d]

    # 2.1) 가보지 않은 칸 존재
    if visited[nx][ny] == 0 and grid[nx][ny] == 0:
        visited[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 2.2) 가보지 않은 칸 존재X or 바다
    else:
        turn_time += 1

    # 네 방향 모두 못 감
    if turn_time == 4:
        nx = x - dx[d]
        ny = y - dy[d]

        ## 뒤로 이동 가능
        if grid[nx][ny] == 0:
            x = nx
            y = ny
        ## 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0


print(count)
        


