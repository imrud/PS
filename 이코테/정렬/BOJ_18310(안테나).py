import sys
input = sys.stdin.readline

## 0. 입력
n = int(input())    ##
house = list(map(int, input().split()))
house.sort()

## 문제 잘 읽기
# minValue = 0    ## 안테나까지의 최소거리
# if n % 2:
#     mid = n // 2 + 1
# else:
#     mid = n // 2
#
# for i in range(n):
#     if mid == i:
#         minValue += 0
#     else:
#         minValue += abs(house[mid]-house[i])

print(house[(n-1)//2])

