import sys
import heapq

input = sys.stdin.readline
INF =int(1e9)

V, E = map(int, input().split())    ## 정점의 개수, 간선의 개수 입력 받기
K = int(input())        ## 시작 정점 입력 받기
graph = [[] for _ in range(V+1)]     ## 정점을 입력 받을 리스트
distance = [INF for _ in range(V+1)]    ## 시작점과 각 노드의 최소 거리를 나타낼 리스트

for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))     ## u에서 가는 노드의 번호와 가중치를 저장

def dijkstra(K):
    que = []
    distance[K] = 0     ## 시작 노드의 최소 거리는 0(자기 자신은 0)
    heapq.heappush(que, (0, K))

    while que:
        dist, now = heapq.heappop(que)      ## 최소 거리가 짧은 노드부터, 최소거리-노드 번호 꺼내기
        if distance[now] < dist:    ## 꺼낸 값보다 기존의 값이 작다면 상태 유지
            continue

        for i in graph[now]:

            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(que, (cost, i[0]))

dijkstra(K) ## 시작은 K부터

for i in range(1, V+1):
    if distance[i] == INF:  ## 시작노드에서 해당 노드로부터 도달하지 못한 경우
        print("INF")
    else:   ## 시작 노드로에서 해당 노드로부터 도달한 경우
        print(distance[i])
