## 백준 : 1406
import sys
input = sys.stdin.readline

word = list(input().strip())    ## 커서 기준 왼쪽
n = len(word)                   ## 커서 기준 오른쪽
stack = []

for _ in range(int(input())):
    line = list(input().split())

    if line[0] == 'L':
        if word:
            stack.append(word.pop())
        
    elif line[0] == 'D':
        if stack:
            word.append(stack.pop())
            
        
    elif line[0] == 'B':
        if word:
            word.pop()
        
    elif line[0] == 'P':
        word.append(line[1])

word.extend(reversed(stack))
print(''.join(word))
    
    
    
               
               
