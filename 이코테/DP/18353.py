## 이코테[백준] - 18353
import sys
input = sys.stdin.readline

n = int(input())
army = list(map(int, input().split()))

count = [1]*n  ## 가장 긴 감소하는 수열의 길이 저장

for i in range(1, n):
    for j in range(0, i):
        if army[j] > army[i]:
            count[i] = max(count[i], count[j]+1)
            
print(n-max(count))


