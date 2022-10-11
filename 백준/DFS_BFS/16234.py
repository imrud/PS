## 백준 - 인구이동 : 16234
import sys
from collections import deque
input = sys.stdin.readline

n, l, r = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count = 0

def bfs(x, y, index):
    united[]
    united.append((x, y))

    que = deque()
    que.append((x, y))
    unio[x][y] == index         ## 현재 연합 번호 할당
    summary = graph
    que 


result = 0
## 더 이상의 인구 이동 할 수 없을때까지 반복
while True:
    union = [[-1]*n for_ in range(n)]
    index = 0

    for i in range(n):
        for j in rnage(n):
            if union[i][j] == -1:       ## 아직 방문
                bfs(i, j, index)
                index += 1

    ## 모든 인구 이동이 끝난 경우
    if index == n*n:
        break
    result = += 1

print(result)
    



