import sys
input = sys.stdin.readline
def count_x(arr, x):
    n = len(arr)

    ## x가 처음 등장하는 인덱스 계산
    f_idx = first(arr, x, 0, n-1)

    ## 수열에 x가 존재하지 않는 경우, 0반환
    if f_idx == None:
        return 0

    # x가 마지막으로 등장하는 인덱스 계산
    e_idx = last(arr, x, 0, n-1)

    ## 개수니까 1더해야됨
    return e_idx - f_idx + 1

def first(arr, target, start, end):
    if start > end:
        return None

    mid = (start+end)//2

    ## 배열 첫번째 요소가 target 이거나, id 이전 값은 target 보다 작으면서 mid가 target인 경우 -> 첫 시작
    if (mid == 0 or target > arr[mid-1]) and arr[mid] == target:
        return mid
    ## mid의 값보다 target이 작은 경우 -> mid 기준 왼쪽확인
    elif arr[mid] >= target:
        return first(arr, target, start, mid-1)
    ## target 값이 mid 값보다 큰 경우 -> mid 기준 오른쪽 확인
    else:
        return first(arr, target, mid+1, end)

def last(arr, target, start, end):
    if start > end:
        return None

    mid = (start+end)//2

    ## mid가 배열의 끝이거나(=마지막 요소가 target)/
    ## mid 다음값이 target보다 크면서 mid가 target인 경우 -> target의 끝
    if (mid == len(arr) - 1 or target < arr[mid+1]) and arr[mid] == target:
        return mid
    ## mid의 값보다 target이 작은 경우 -> mid 기준 왼쪽확인
    elif arr[mid] > target:
        return last(arr, target, start, mid-1)
    ## target 값이 mid 값보다 큰 경우 -> mid 기준 오른쪽 확인
    else:
        return last(arr, target, mid+1, end)



N, x = map(int, input().split())
arr = list(map(int, input().split()))

# 값이 x인 데이터 개수 계산
cnt = count_x(arr, x)

if cnt == 0:        ## x이 원소가 존재하지 X
    print(-1)
else:
    print(cnt)

## 시작복잡도 O(n)
##print(arr.count(x))