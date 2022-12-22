import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

## 노드의 개수, 간선의 개수, 시작 노드를 입력받기
n, m, start = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

## 모든 간선 정보를 입력받기
for _ in range(m):
    x, y, z = map(int, input().split())
    ## x번 노드에서 y번 노드로 가는 비용이 z라는 의미
    graph[x].append((y, z))

def dijkstra(start):
    que = []
    heapq.heappush(que, (0, start))
    distance[start] = 0
    while que:
        ## 가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
        dist, now = heapq.heappop(que)
        if distance[now] < dist:
            continue

        ## 현재 노드와 연결도니 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]

            ## 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(que, (cost, i[0]))


## 다익스트라 알고리즘을 수행
dijkstra(start)

## 도달할 수 있는 노드의 개수
cnt = 0
max_distance = 0
for d in distance:
    if d != INF:
        cnt += 1
        max_distance = max(max_distance, d)

## 시작 노드는 제외해야 하므로 count - 1을 출력
print(cnt - 1, max_distance)