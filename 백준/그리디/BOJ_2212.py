import sys

input = sys.stdin.readline

N = int(input())    ## 고속도로 위 센서 개수
K = int(input())    ## 집중국 개수
array = sorted(list(map(int, input().split(' '))))     ## 센서들의 좌표 -> 오름차순 정렬

dist = []

for i in range(N-1):
    dist.append(array[i+1] - array[i])      ## 센서들의 사이 거리 구하기

dist.sort(reverse=True)     ## 거리 내림차순으로 정렬

print(sum(dist[K-1:]))      ## 가장 큰 K-1개를 제외한 나머지 거리들의 합 = 수신 가능 영역 길이의 합의 최소값


