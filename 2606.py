#백준2606
import sys
import sys
sys.setrecursionlimit(10000)        ## python 재귀한도 늘려주기

##1. 
cp = int(sys.stdin.readline())      ## 컴퓨터의 수(정점)
ncp = int(sys.stdin.readline())     ## 연견된 컴퓨터 쌍의 수(간선)
graph = [[] for _ in range(cp+1)]
##visited = []
visited = [0]*(cp+1)

## 2.
for _ in range(ncp):
    u, v = map(int, sys.stdin.readline().split(' '))    ## 간선의 양 끝점 u, v
    graph[u].append(v)
    graph[v].append(u)

##3.
##def dfs(start):
##    for i in graph[start]:
##        if i not in visited:
##            visited.append(i)
##            dfs(i)
##    return len(visited)
def dfs(start):
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            dfs(i)

dfs(1)    
print(sum(visited)-1)
