## 백준: 9012
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    ps = list(input().strip())
    stack = []
    isEmpty = False
    
    for char in ps:
        if char == '(':
            stack.append(char)
        else:
            if len(stack) == 0:      ## 스택이 비어있을 경우
                isEmpty = True
                break
            else:
                stack.pop()
                
    if not stack and not isEmpty:       ## 스택이 비어있고, False인 경
        print('YES')
    else:
        print('NO')
