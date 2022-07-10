#백준 11724 : 연결 요소의 개수
import sys
sys.setrecursionlimit(10000)        ## python 재귀한도 늘려주기

n, m = map(int, sys.stdin.readline().split(' '))    ## n:정점, m:간선
graph = [[] for _ in range(n+1)]
visited=[False]*(n+1)
cnt = 0     ## 연결요소 값

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split(' '))    ## 간선의 양 끝점 u, v
    graph[u].append(v)
    graph[v].append(u)

def dfs(p):
    visited[p] = True   ## 방문 OK
    for i in graph[p]:
        if not visited[i]:
            dfs(i)

for i in range(1, n+1):
    if visited[i] == False:     ## 해당 노드 아직 방문 전
        dfs(i)
        cnt += 1
        
print(cnt)
