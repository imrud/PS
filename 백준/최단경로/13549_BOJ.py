import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)  ## 최댓값 설정

N, K = map(int, input().split())    ## 수빈이와 동생의 위치 입력받기

def dijkstra(N, K):
    dist = [INF]*100001     ## 점의 최대 범위까지, 최소 시간을 담을 리스트를 무한대로 초기화해서 생성하기
    dist[N] = 0     ## 초기 수빈이의 위치에서의 시간은 0으로 설정
    que = []
    heapq.heappush(que, (0, N))     ##(걸린 시간, 수빈이의 위치)를 우선순위 큐에 넣기

    while que:
        t, loc = heapq.heappop(que)     ## 최소 시간인 원소 빼기
        for nx in [(loc + 1, 1), (loc - 1, 1), (loc * 2, 0)]:     ## (이동 가능 경로, 경로에 따른 시간)
            ## nx[0]이 점의 범위내에 위치 & 해당 점의 최소 위치가 큐에서 빼낸값에 이동시간 더한 값보다 작을 경우
            if 0 <= nx[0] < 100001 and dist[nx[0]] > t + nx[1]:
                dist[nx[0]] = t + nx[1]     ## 해당 위치에 따른 최소 시간 갱신하기
                heapq.heappush(que, (dist[nx[0]], nx[0]))
    print(dist[K])      ## K의 최소 시간 비용 출력하기(결과값)

dijkstra(N, K)      ## 다익스트라 함수 실행하기



