## 부품 찾기
import sys
input = sys.stdin.readline

## 내풀이
##n = int(input())
##inventory = list(map(int, input().split()))
##
##m = int(input())
##order = list(map(int, input().split()))
##
##for i in order:
##    if i in inventory:
##        print("yes", end=' ')
##    else:
##        print("no", end= ' ')


## 이진탐색 이용
def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start+end) // 2

        ## 찾은 경우 인덱스 반환
        if arr[mid] == target:
            return mid
        
        elif arr[mid] > target:
            end = mid - 1
            
        else:
            start = mid + 1

    return None


n = int(input())
inv = list(map(int, input().split()))
inv.sort()      ## 이진 탐색 수행 위해 사전에 정렬

m = int(input())
order = list(map(int, input().split()))

for i in order:
    ## 배열, target, start, end
    res = binary_search(inv, i, 0, n-1)
    if res != None:
        print("yes", end=' ')
    else:
        print("no", end= ' ')
