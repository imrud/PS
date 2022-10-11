## 백준 : 5567
import sys
sys.setrecursionlimit(5000000)      ##  재귀 깊이 변경
from collections import deque
input = sys.stdin.readline


def bfs(num):
    que = deque()
    visited[num] = 1    # 방문확인
    que.append(num)

    while que:
        v = que.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                que.append(i)
                visited[i] = visited[v] + 1
    


n = int(input())
m = int(input())

## 방문 확인
visited = [0 for i in range(n+1)]   ## 1부터 사용하기때문에 n+1로 설정

## 그래프
graph = [[] for _ in range(n+1)]
for i in range(m):
    x, y = map(int, input().strip().split())
    graph[x].append(y)
    graph[y].append(x)

bfs(1)  ## 상근이부터 시작(== 1)

res = 0
for i in range(2, n+1):
    if visited[i] < 4 and visited[i] != 0:
        res += 1

print(res)
        

    
        
