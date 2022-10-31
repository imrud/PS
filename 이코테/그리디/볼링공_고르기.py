## 볼링공 고르기
import sys
from itertools import combinations

input = sys.stdin.readline

## 아이디어
## 조합에서 중복되는 수 빼기

n, m = map(int, input().split())
nums = list(map(int, input().split()))

## 중복 되는 숫자 카운트
cnt = [0] * (n+1)

for i in nums:
    cnt[i] += 1

minus = 0
for j in range(1, len(cnt)):
    if cnt[j] > 1:
        minus += 1


print(len(list(combinations(nums, 2))) - minus)
