## 백준 : 2749
import sys
input = sys.stdin.readline

def fib(n):
    x, y = 0, 1

    for i in range(0, n):
        x, y = y, x+y

    return x

n = int(input())

print(fib(n))
