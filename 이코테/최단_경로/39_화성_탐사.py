import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)  ## 무한 값 설정

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

## 테스트 케이스의 수만큼 반복
for _ in range(int(input())):
    n = int(input())    ## 노드의 개수 입력받기

    ## 전체 맵 정보를 입력받기
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    ## 최단 거리 테이블을 모두 무한으로 초기화
    distance = [[INF] * n for _ in range(n)]

    x, y = 0, 0 ## 시작 위치 (0,0)
    que = [(graph[x][y], x, y)]     ## 우선순위는 해당 좌표의 비용
    distance[x][y] = graph[x][y]    ## 사작 좌표의 거리는 graph값으로 설정

    ## 다익스트라 알고리즘 수행
    while que:
        dist, x, y = heapq.heappop(que) ## 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        ## 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[x][y] < dist:
            continue
        ## 현재 노드와 연결된 인접 노드 확인하기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            ## 맵의 범위를 벗어나는 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            cost = dist + graph[nx][ny]
            ## 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우 -> 거리 갱신 후 힙에 넣기
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(que, (cost, nx, ny))


    print(distance[n-1][n-1])

