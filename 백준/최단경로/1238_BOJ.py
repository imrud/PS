## 백준 1238 : 파티
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)      ## 최대값 설정

N, M, X = map(int, input().split())     ## 마을 개수(노드 개수), 도로 개수(간선 개수), 파티 장소
graph = [[] for i in range(N+1)]    ## 도로 간의 정보를 담을 리스트 생성

for _ in range(M):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))     ## 도로 정보  추가하기

def dijkstra(X):
    distance = [INF for _ in range(N+1)]    ## 최소 거리를 저장할 리스트 생성
    que = []

    heapq.heappush(que, (0, X))  ## 우선 순위 큐에 (버스 비용, 도시) 삽입
    distance[X] = 0

    while que:
        dist, now = heapq.heappop(que)  ## 우선 순위 큐에서 최소 버스 비용이 작은 출발 도시부터 꺼내기

        if distance[now] < dist:  ## 꺼낸 값보다 기존의 값이 작다면 상태 유지
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(que, (cost, i[0]))

    return distance     ## 반복문 마친 후, 최소 비용 반환

back = dijkstra(X)      ## X에서 각 노드로 가는 최소 비용
result = 0
for i in range(1, N+1):
    go = dijkstra(i)    ## 각 노드에서 x로 가는 경우의 최소 비용
    result = max(result, go[X]+back[i])     ## 최대값 구하기

print(result)


# #### 내가 만든 코드
# # g_distance = [INF for i in range(N+1)]    ## 각 마을(노드)마다의 최소 거리 비용 구하기
# tmp = [0 for i in range(N+1)]
# h_distance = [INF for i in range(N+1)]    ## 각 마을(노드)마다의 최소 거리 비용 구하기
#
# for _ in range(M):
#     a, b, t = map(int, input().split())
#     graph[a].append((b, t))     ## 도로 정보  추가하기
#
# def go_party(X):
#     que = []
#     g_distance[X] = 0
#     heapq.heappush(que, (0, X))  ## 우선 순위 큐에 (버스 비용, 도시) 삽입
#
#     while que:
#         dist, now = heapq.heappop(que)  ## 우선 순위 큐에서 최소 버스 비용이 작은 출발 도시부터 꺼내기
#         if g_distance[now] < dist:  ## 꺼낸 값보다 기존의 값이 작다면 상태 유지
#             continue
#
#         for i in graph[now]:
#             cost = dist + i[1]
#
#             if cost < g_distance[i[0]]:
#                 g_distance[i[0]] = cost
#                 heapq.heappush(que, (cost, i[0]))
#
#
#
# def comeback_home(X):
#     que = []
#     h_distance[X] = 0
#     heapq.heappush(que, (0, X))  ## 우선 순위 큐에 (버스 비용, 도시) 삽입
#
#     while que:
#         dist, now = heapq.heappop(que)  ## 우선 순위 큐에서 최소 버스 비용이 작은 출발 도시부터 꺼내기
#         if h_distance[now] < dist:  ## 꺼낸 값보다 기존의 값이 작다면 상태 유지
#             continue
#
#         for i in graph[now]:
#             cost = dist + i[1]
#
#             if cost < h_distance[i[0]]:
#                 h_distance[i[0]] = cost
#                 heapq.heappush(que, (cost, i[0]))
#
# ## 각 마을에서 X까지의 최소 거리 구하기
# for i in range(N):
#     g_distance = [INF for _ in range(N + 1)]  ## 각 마을(노드)마다의 최소 거리 비용 구하기
#     if i+1 != X:
#         go_party(i+1)
#         tmp[i+1] = g_distance[2]
# comeback_home(X)    ## X로부터 각 마을까지의 최소 거리
# # print(tmp)
# # print(h_distance)
#
# max_tmp = 0
# for i in range(1, N+1):
#     if tmp[i]+h_distance[i] > max_tmp:
#         max_tmp = tmp[i]+h_distance[i]
#
# print(max_tmp)