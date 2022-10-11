## 백준 : 11286
import sys
import heapq
input = sys.stdin.readline
##heap = []
##
##for _ in range(int(input())):
##    x = int(input())
##
##    if x == 0:
##        if not heap:
##            print(0)
##        else:
##            print(heapq.heappop(heap)[1])
##    else:
##        heapq.heappush(heap, (abs(x), x))



## 배열 두 개로 풀기
pq = []     ## 양수 큐
mq = []     ## 음수 큐

for _ in range(int(input())):
    x = int(input())

    if x > 0:       ## 양수일 경우 그대로
        heapq.heappush(pq, x)
    elif x < 0:     ## 음수일 경우 절대값으로 넣기
        heapq.heappush(mq, -x)

    elif not pq and not mq:     ## 둘 다 비어있을 때
        print(0)

    elif not pq:    ## 음수 큐에서 출력
        print(-heapq.heappop(mq))
    elif not mq:    ## 양수 큐에서 출력
        print(heapq.heappop(pq))
        
    elif pq[0] >= mq[0]:
        print(-heapq.heappop(mq))
    else:
        print(heapq.heappop(pq))
    
