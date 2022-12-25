## (백준)1916: 최소비용 구하기
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

N = int(input())    ## 도시의 개수
M = int(input())    ## 버스의 개수
graph = [[] for _ in range(N+1)]    ## 출발 도시에 따른 버스 정보(도착 도시 번호, 버스 비용)를 담을 리스트 생성
min_cost = [INF for _ in range(N+1)]    ## 각 도시의 거리 최소 값

for _ in range(M):
    s, d, w = map(int, input().split())     ## 출발 도시의 번호, 도착 도시의 번호, 버스 비용 입력 받기
    graph[s].append((d,w))     ## 출발 도시에 따라 (도착 도시 번호, 버스 비용)을 그래프에 삽입

start, end = map(int, input().split())  ## 문제에서 구하려는 출발하는 도시, 도착하는 도시 번호 입력 받기

def dijkstra(start):
    que = []
    min_cost[start] = 0
    heapq.heappush(que, (0, start))     ## 우선 순위 큐에 (버스 비용, 도시) 삽입

    while que:
        dist, now = heapq.heappop(que)  ## 우선 순위 큐에서 최소 버스 비용이 작은 출발 도시부터 꺼내기
        if min_cost[now] < dist:  ## 꺼낸 값보다 기존의 값이 작다면 상태 유지
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < min_cost[i[0]]:
                min_cost[i[0]] = cost
                heapq.heappush(que, (cost, i[0]))

dijkstra(start)
print(min_cost[end])