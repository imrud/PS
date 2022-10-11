## 백준 : 14502 - 연구소
import sys
from collections import deque
from itertools import combinations
import copy

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    t_graph = copy.deepcopy(graph)
    que = deque(virus)

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if t_graph[nx][ny] == 0:
                    t_graph[nx][ny] = 2
                    que.append((nx, ny))

    count = 0
    for i in range(n):
        for j in range(m):
            if t_graph[i][j] == 0:
                count += 1
    return count


n, m = map(int, input().split())

graph = []
empty = []         ## 빈 칸
virus = []          ## 바이러스


for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] == 0:        ## 빈칸 그래프 추가
            empty.append((i, j))
        if graph[i][j] == 2:        ## 바이러스 그래프 추가
            virus.append((i, j))
            

max_count = 0      ## 반환할 최대값
for data in list(combinations(empty, 3)):
    for x, y in data:
        graph[x][y] = 1       ## 벽 세우기
    max_count = max(max_count, bfs())

    for x, y in data:
        graph[x][y] = 0     ## 다시 빈칸
    
print(max_count)
    
