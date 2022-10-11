## 백준 : 2812
import sys
n, k = map(int, input().split())
nums = list(input().rstrip())

stack = []
tk = k      ## 변화되는 k값 저장하는 변수
for i in range(n):
    while tk > 0 and stack and stack[-1] < nums[i]:
        stack.pop()
        tk -= 1
    stack.append(nums[i])

print(''.join(stack[:n-k]))
