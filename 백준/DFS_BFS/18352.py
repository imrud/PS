## 백준 : 18352 - 특정 거리의 도시 찾기
import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

dis = [-1] * (n+1)  ## 거리
dis[x] = 0      ## 시작노드는 0

#bfs
que = deque([x])
while que:
    v = que.popleft()

    for i in graph[v]:`     `
        if dis[i] == -1:
            dis[i] = dis[v] + 1
            que.append(i)
    
if k in dis:
    for i in range(1, n+1):
        if dis[i] == k:
            print(i)
else:
    print(-1)
    
