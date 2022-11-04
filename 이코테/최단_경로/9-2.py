## 개선된 다익스트라 알고리즘 소스코드
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)      ## 무한 의미하는 값으로 10억 설정(실수처리 방지위해 int로 변환)

n, m = map(int, input().split())    ## 노드, 간선 개수
start = int(input())    # 시작노드 설정
graph = [[] for _ in range(n+1)]    ## 각 노드와 연결된 노드 정보 담는 리스트
visited = [False] * (n+1)    ## 방문 확인 리스트(각 노드 번호가 인덱스므로, n+1로 설정
distance = [INF] * (n+1)    ## 최단 거리 테이블 모두 무한으로 초기화

## 모든 간선 정보 입력 받기
for _ in range(m):
    a, b, c = map(int, input().split()) 
    graph[a].append((b, c))     ## a 노드 -> b노드까지 걸리는 값, c


def dijkstra(start):
    que = []

    #3 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(que, (0, start))
    distance[start] = 0     ## 시작노드 초기화

    while que:  ## 큐가 비어 있지 않다면
        dist, now = heapq.heappop(que)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(que, (cost, i[0]))


## 다익스트라 알고리즘 수행
dijkstra(start)

## 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")   ## 도달한 최단거리 없음

    else:
        print(distance[i])
