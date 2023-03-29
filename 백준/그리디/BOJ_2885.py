import sys

input = sys.stdin.readline

K = int(input())        ## 꼭 먹어야하는 초콜릿의 개수
size = 1        ## 초콜릿 크기 변수
cnt = 0     ## 초콜릿을 자르는 횟수
while size < K:
    size = size << 1    ## 왼쪽으로 움직이기(2의 제곱만큼 커짐)
## 다른 구현
while size < K:
    size *= 2

min_size = size ## 최소 크기

while K > 0:            ## K가 (먹어야하는 초콜릿) 0이 되지 않을 때까지 반복
    if K >= size:       ## 먹어야하는 초콜릿이 size보다 크거나 같을 경우
        K -= size       ## K에서 같게 된 초콜릿수를 빼기
    else:
        size //= 2      ## size를 반 나누기
        cnt += 1        ## 나눈 횟수 증가

print(min_size, cnt)