##백준 : 1927
import heapq    
import sys
input = sys.stdin.readline


heap = []    ## 힙 생성

for _ in range(int(input())):
    x = int(input())

    if x != 0:      ## x가 자연수일 경우
        heapq.heappush(heap, x)

    else:
        if heap:
            print(heapq.heappop(heap))
        else:       ## 빈 배열일 때
            print(0)


    
               
