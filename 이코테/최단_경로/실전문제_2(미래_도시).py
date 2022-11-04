## 미래도시
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

graph = [[INF]*(n+1) for _ in range(n+1)]   ## 2차원 리스트 생성, 무한으로 초기

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0     ## 자기자신 -> 자기자신은 0으로

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1     ## 양방향이니
x, k = map(int, input().split())    ## 최종목적지, 중간 경유지

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

res = graph[1][k] + graph[k][x]
if res >= INF:
    print("-1")
else:
    print(res)

