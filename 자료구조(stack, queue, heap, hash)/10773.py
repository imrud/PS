## 백준 : 10773
import sys
##input = sys.stdin.readline

stack = []
    
##for i in range(int(input())):
##    n = int(input())
##    if n != 0:
##        stack.append(n)
##    else:
##        stack.pop()
##
##print(sum(stack))


k = int(input())

for i in map(int, sys.stdin.read().split()):
    if i:
        stack.append(i)
    else:
        stack.pop()
print(sum(stack))
    
