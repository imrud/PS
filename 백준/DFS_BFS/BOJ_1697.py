from collections import deque
import sys

input = sys.stdin.readline
MAX = 10**5     ## 최대값 설정 / 보기 조건 참고 (0 ≤ N ≤ 100,000)
N, K = map(int, input().split())    ## 수빈, 동생 위치

dist = [0]*(MAX+1)  ## 이동거리 확인하기 위해(인덱스 바로 집어넣기 위해 +1)

def bfs():
    que = deque()
    que.append(N)

    while que:
        x = que.popleft()

        if x == K:
            print(dist[x])
            break

        for nx in [x-1, x+1, 2*x]:      ## x-1, x+1, 2*x 를 한 사이클로
            if 0 <= nx <= 100000 and not dist[nx]:
                dist[nx] = dist[x]+1
                que.append(nx)


bfs()