## 간단한 다익스트라 알고리즘 소스코드
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


##  방문하지 않은 노드 중, 가자 ㅇ최단 거리가 짧은 노드 번호 반환
def get_samllest_node():
    min_value = INF     ## 최솟값을 INF로 설정
    index = 0
    
    for i in range(1,n+1):
        if distance[i] < min_value and not visited[i]:
          min_value = distance[i]
          index = i

    return index


def dijkstra(start):
    distance[start] = 0     ## 시작노드 초기화
    visited[start] = True   ## 시작노드 방문처리

    for j in graph[start]:      ## j는 (b, c)로 이루어짐
        distance[j[0]] = j[1]


    for i in range(n-1):
        ## 현재 최단 거리가 가장 짧은 노드 꺼내서 방문처리
        now = get_samllest_node()
        visited[now] = True

        for j in graph[now]:        ## j는 (b, c)
            cost = distance[now] + j[1]     ## 현재까지의 값 + 거리
            if cost < distance[j[0]]:      # 갱신
                distance[j[0]] = cost
             


## 다익스트라 알고리즘 수행
dijkstra(start)

## 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    if distance[i] == INF:  ## 해당 노드의 최단경로에 도달하지 못함
        print("INFINITY")
    else:   ## 도달한 경우 거리 출력력
        print(distance[i])
    
