## 곱하기 혹은 더하기
import sys
input = sys.stdin.readline

nums = input().strip()

res = 0
for n in nums:
    n = int(n)
    if n <= 1 or res <= 1:
        res += n
    else:
        res *= n


print(res)
