import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())    ## 헛간 개수(노드 수), 통로 수(간선 개수) 입력 받기
start = 1   ## 시작 노드를 1번 헛간으로 설정(출발은 항상 1번)
graph = [[]*(n+1) for _ in range(n+1)]  ## 각 노드에 연결되어있는 노드에 대한 정보 담는 리스트 생성

## 정답 코드
distance = [INF]*(n+1)  ## 최단 거리 테이블을 모두 무한으로 초기화
for _ in range(m):
    a, b = map(int, input().split())
    ## a <-> b 이동 비용은 1 (양방향이므로 둘 다 설정해야한다)
    graph[a].append((b, 1))
    graph[b].append((a, 1))

def dijkstra(start):
    que = []
    heapq.heappush(que, (0, start)) ## 시작노드를 우선순위 큐에 넣기
    distance[start] = 0  ## 시작노드 거리는 0으로 설정

    while que:
        dist, now = heapq.heappop(que)      ##  가장 최단 거리가 짧은 노드 꺼내기 (거리, 노드번호)
        if distance[now] < dist:    ## 현재 노드가 이미 처리된 적이 있는 노드라면 무시
            continue

        for i in graph[now]:    ## 현재 노드와 연결된 다른 인접한 노드들을 확인
            cost = dist + i[1]  ## i는 (연결된 노드 번호, 비용) 으로 구성

            if cost < distance[i[0]]:  ## 현재 노드 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
                distance[i[0]] = cost
                heapq.heappush(que, (cost, i[0]))      ## 큐에 (거리, 노드번호) 삽입

## 내코드
# distance = [0 for _ in range(n+1)]
#
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
#
# def dijkstra(start):
#     que = []
#     heapq.heappush(que, (0, start))
#     #distance[start] = 0  ## 시작노드 초기화
#
#     while que:
#         dist, now = heapq.heappop(que)      ## 거리, 노드 번호
#         if distance[now] > dist:
#             continue
#
#         for i in graph[now]:
#             cost = dist + 1
#
#             if distance[i] == 0 and i != 1:
#                 distance[i] = cost
#                 heapq.heappush(que, (cost, i))


## 다익스트라 알고리즘 실행
dijkstra(start)
print(distance)
## 정답코드시 추가해야할 코드
distance = distance[1:]
print(distance.index(max(distance)) + 1, max(distance), distance.count(max(distance)))

## 숨어야 하는 헛간의 번호, 해당 헛간까지의 거리, 해당 헛간과 같은 거리를 같는 헛간의 개수 출력
# print(distance.index(max(distance)), max(distance), distance.count(max(distance)))