## 백준 : 1427
import sys
input = sys.stdin.readline

num = list(input().rstrip())

num.sort(key = lambda x: int(x), reverse=True)

print(''.join(num))
