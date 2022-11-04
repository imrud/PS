## 플로이드 워셜 알고리즘 소스코드
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF]*(n+1) for _ in range(n+1)]   ## 2차원 리스트 생성, 무한으로 초기

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0     ## 자기자신 -> 자기자신은 0으로


## 간선에 대한 정보 입력받아, 그 값으로 초기화
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c


## 점화식에 따라 알고리즘 실행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])


## 수행된 결과 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == "INF":
            print("INFINITY", end=' ')
        else:
            print(graph[a][b], end=' ')
    print()
