import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)  ## 최대값 설정

N, E = map(int, input().split())    ## 정점의 개수, 간선의 개수 입력받기
graph = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))     ## 정방향 그래프에 입력하기
    graph[b].append((a, c))   ## 역방향 그래프에 입력하기

u, v = map(int, input().split())

def dijkstra(start):
    distance = [INF for _ in range(N + 1)]      ## 최소 거리를 저장할 리스트
    distance[start] = 0     ## 시작노드의 최소 거리는 0

    que = []
    heapq.heappush(que, (0, start))

    while que:
        dist, now = heapq.heappop(que)  ## 우선순위 큐에서 가장 작은 비용부터 꺼내기
        if distance[now] < dist:  ## 꺼낸 값보다 기존의 값이 작다면 상태 유지
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(que, (cost, i[0]))

    return distance

d1 = dijkstra(1)
d2 = dijkstra(u)
d3 = dijkstra(v)

#result = min(d1[u]+d2[v]+d3[N], d1[v]+d3[u]+d2[N])
if min(d1[u]+d2[v]+d3[N], d1[v]+d3[u]+d2[N]) < INF:
    print(min(d1[u]+d2[v]+d3[N], d1[v]+d3[u]+d2[N]))
else:
    print(-1)


# ## 내풀이
# tmp = [1, u, v, N]  ## 진행 경로
# result = 0
# for i in range(len(tmp)-1):
#     t_dist = dijkstra(tmp[i+1])
#     if t_dist[tmp[i]] == INF:   ## 최소 경로가 존재하지 않는 경우
#         result = -1
#         break
#     else:
#         #print(t_dist[tmp[i]])
#         result += t_dist[tmp[i]]
#
# print(result)



