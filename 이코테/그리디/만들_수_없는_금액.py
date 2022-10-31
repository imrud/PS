## 만들 수 없는 금
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

target = 1      ## 내가 만들 수 없는 
data.sort()     ## 오름차순 정렬

for i in data:
    if target < i:
        break
    else:
        target += i

print(target)
