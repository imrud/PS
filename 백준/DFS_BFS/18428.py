## 백준 - 18428 : 감시자 피하기
import sys
import copy
from collections import deque
from itertools import combinations

input = sys.stdin.readline

n = int(input())
graph = []
teacher = []        ## 선생님 위치 
blank = []          ## 공백 위치

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    graph.append(list(input().split()))
    for j in range(n):
        if graph[i][j] == 'T':
            teacher.append((i, j))      ## 위치를 튜플로 저장
        elif graph[i][j] == 'X':
            blank.append((i, j))

def bfs():      ## 학생 찾으면 False 반환
    que = deque(teacher)
    t_graph = copy.deepcopy(graph)
    while que:
        x, y = que.popleft()
        for i in range(4):
            tx, ty = x, y

            while True:
                nx = tx + dx[i]
                ny = ty + dy[i]

                if 0 <= nx < n and 0 <= ny < n:    ## 범위 체크
                    if t_graph[nx][ny] == 'X':
                        t_graph[nx][ny] = 'T'
                        
                    elif t_graph[nx][ny] == 'S':    ## 학생 찾으면 Flase 반환
                        return False
                    
                    elif t_graph[nx][ny] == 'O':
                        break
                    
                    tx, ty = nx, ny
                    
                else:
                    break
    return True
                
                        
cehck = False
for data in list(combinations(blank, 3)):   ## 3개씩 조합 
    for x, y, in data:
        graph[x][y] = 'O'       ## 벽 표시

    if bfs():
        cehck = True
        break
    
    for x, y in data:           ## false면 해당자리 다시 'X'로 표시 
        graph[x][y] = 'X'


if cehck:
    print("YES")
else:
    print("NO")
