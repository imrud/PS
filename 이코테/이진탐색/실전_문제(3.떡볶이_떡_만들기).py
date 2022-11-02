## 떡볶이 떡 만들기
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))


## 내 풀이
##data.sort(reverse = True)
##
##target = data[0]
##
##while target > 0:
##    res = 0
##    for i in range(n):
##        if data[i] - target > 0:
##            res += data[i] - target
##
##    if res == m:
##        print(target)
##        break
##    else:
##        target -= 1


## 해설
start = 0
end = max(data)

res = 0
## 이진 탐색 수행
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in data:
        if x > mid:
            total += x - mid

    if total < m:   ## 떡이 부족 -> 더 많이 자르기 -> 왼쪽 부분 탐색
        end = mid - 1
    else:
        res = mid
        start = mid + 1     ## 최대한 덜 잘랐을 때를 찾으니 높이 증가하며 더 찾기

print(res)
