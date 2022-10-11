## 백준 18405 : 경쟁적 전염
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

area = []
virus = []      ## 바이러스 저장 
for i in range(n):
    area.append(list(map(int, input().split())))
    for j in range(n):
        if area[i][j] != 0:
            virus.append((area[i][j], i, j, 0))     ## 바이러스 조류, x,y위치, 시간

s, tx, ty = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
                         
virus.sort()
que = deque(virus)

while que:
    v_type, x, y, time = que.popleft()

    if time == s:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if area[nx][ny] == 0:
                area[nx][ny] = v_type
                que.append((v_type, nx, ny, time+1))
                


print(area[tx-1][ty-1])
