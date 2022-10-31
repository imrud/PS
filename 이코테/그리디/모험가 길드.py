## 모험가 길드
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

## 오름차순 정렬
arr.sort()

## 공포도 확인
result = 0
count = 0

for i in range(len(arr)):
    count += 1
    if count >= i:
        result += 1     ## 그룹 증가
        count = 0       ## 초기화

print(result)

    
