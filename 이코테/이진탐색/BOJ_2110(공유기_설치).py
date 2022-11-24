import sys
input = sys.stdin.readline

## 0. 입력받기
N, C = map(int, input().split())
house = [int(input()) for _ in range(N)]

# for _ in range(N):
#     house.append(int(input()))

## 1. 오름차순 정렬
house.sort()
start = 1   ## 가능한 최소 거리
end = house[-1] - house[0]      ## 가능한 최대 거리
res = 0

while(start <= end):
    mid = (start+end)//2
    val = house[0]
    cnt = 1

    for i in range(1, N):
        if house[i] >= val + mid:
            val = house[i]
            cnt += 1
    if cnt >= C:
        start = mid + 1
        res = mid
    else:
        end = mid -1

print(res)
