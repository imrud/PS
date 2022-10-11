import sys
input = sys.stdin.readline

##def push(num):
##    stack.append(num)
##    
##def pop():
##    if len(stack) != 0:
##        print(stack[-1])
##        stack.pop()
##    else:
##        print(-1)
##
##def size():
##    print(len(stack))
##
##def empty():
##    if len(stack) > 0:
##        print(0)
##    else:
##        print(1)
##
##def top():
##    if len(stack) > 0:
##        print(stack[-1])
##    else:
##        print(-1)


n = int(input())
stack = []
for _ in range(n):
    line = input().split()
    order = line[0]

    if order == "push":
        stack.append(line[1])

    elif order == "pop":
        if len(stack) != 0:
            print(stack.pop())
        else:
            print(-1)

    elif order == "size":
        print(len(stack))

    elif order == "empty":
        if len(stack) > 0:
            print(0)
        else:
            print(1)

    elif order == "top":
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)
        
        
