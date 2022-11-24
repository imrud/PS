import sys
input = sys.stdin.readline

def solve(arr, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if arr[mid] == mid:
        return mid
    ## arr[mid]의 값이 인덱스 mid보다 큰 경우 -> mid 기준 왼쪽 탐색
    elif arr[mid] > mid:
        return solve(arr, start, mid - 1)
    ## arr[mid]의 값이 인덱스 mid보다 작은 경우 -> mid 기준 오른쪽 탐색
    else:
        return solve(arr, start, mid - 1)


#     return solve(arr, start, mid - 1)
# elif arr[mid] < mid:
#     return solve(arr, mid + 1, end)
# else:
#     res.append(mid)

    ## 내 풀이
    # ## arr[mid]의 값이 인덱스 mid보다 작은 경우 -> mid 기준 왼쪽 탐색
    # if arr[mid] > mid:
    #     return solve(arr, start, mid - 1)
    # elif arr[mid] < mid:
    #     return solve(arr, mid + 1, end)
    # else:
    #     res.append(mid)

N = int(input())
arr = list(map(int, input().split()))

idx = solve(arr, 0, N-1)
if idx == None:
    print(-1)
else:
    print(idx)


#### 내 풀이
# global res
# res = []
# solve(arr, 0, N-1)
#
# if res:
#     print(*res)
# else:
#     print(-1)
