## 백준 : 10870
import sys
input = sys.stdin.readline

def fibonacci(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0

    return fibonacci(n-1)+fibonacci(n-2)
    


n = int(input())

f = 0
f1 = 1
print(fibonacci(n))



## if-elif 구문을 다음 아래와 같이 구현 가
##if n < 2:
##    return n
