import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

## 오른차순 정렬
data.sort()
res = 0         ## 그룹 최댓값
cnt = 0         ## 현재 모험가 
for i in data:
    cnt += 1
    if cnt >= i:
        res += 1
        cnt = 0
print(res)
    
