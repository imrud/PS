import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())     ## 정점, 간선, 탐색 시작 번호

graph = [[0]*(N+1) for _ in range(N+1)]  ##  N+1 크기의 배열 생성
d_visited = [False]*(N+1)  ## dfs 방문 확인 리스트
b_visited = [False]*(N+1)  ## bfs 방문 확인 리스트

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

## 깊이 우선 탐색
def dfs(V):
    d_visited[V] = True      ## 현재 노드 방문처리
    print(V, end = " ")     ## 방문한 노드 출력

    for i in range(1, N+1):
        ## i번 노드를 방문하지 않았고, V와 인접할 경우 재귀함수 호출
        if (not d_visited[i] and graph[V][i] == 1):
            dfs(i)


## 너비 우선 탐색
def bfs(V):
    b_visited[V] = True ## 방문 확인
    que = deque()
    que.append(V)

    while que:
        pv = que.popleft()
        print(pv, end = " ")

        for i in range(1, N+1):
            if (not b_visited[i] and graph[pv][i] == 1):
                que.append(i)
                b_visited[i] = True

dfs(V)
print()
bfs(V)