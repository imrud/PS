## 백준 : 17298
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
res = [-1]*n    ## 정답 리스트 '-1'로 초기화
stack = []

for i in range(n):
    while stack and arr[stack[-1]] < arr[i]:
        res[stack.pop()] = arr[i]       ## 결론적으로 pop()(되는 건 i-1번째 인덱스
    stack.append(i)     ## stack 비어있다면 index 추가


print(*res)
