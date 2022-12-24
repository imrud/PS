import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())    ## 도시의 개수 입력
m = int(input())    ## 버스의 개수 입력
graph = [[INF]*(n+1) for _ in range(n+1)]

## 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

## 버스 정보 입력 (시작 도시, 도착 도시, 한 번 타는데 필요한 비용)
for _ in range(m):
    a, b, c = map(int, input().split())
    ## 가장 짧은 간선 정보만 저장
    if c < graph[a][b]:
        graph[a][b] = c


## 점화식에 따라 플로이드 워셜 알고리즘 실행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])


for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()