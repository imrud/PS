## 백준 : 1935
import sys
input = sys.stdin.readline

n = int(input()) 
rear = list(input().strip())
num = [int(input()) for _ in range(n)]
stack = []     ## 식에서의 피연산자

op = ['+', '-', '*', '/']
    
      
for i in rear:
     if i not in op:
          stack.append(num[ord(i) - ord('A')])

     else:     ## 연산자인 경우
          n2 = stack.pop()
          n1 = stack.pop()
          
          if i == '+':
               stack.append(n1+n2)
               
          elif i == '-':
               stack.append(n1-n2)
               
          elif i == '*':
               stack.append(n1*n2)
                    
          elif i == '/':
               stack.append(n1/n2)

print('%.2f'%stack[0])
          
          
      
    
