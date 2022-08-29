## 백준 : 1914
import sys
input = sys.stdin.readline

def hanoi(n, x, y, z):
    if n == 1:
        print(x, z)
        return

    hanoi(n-1, x, z, y)
    print(x, z)

    hanoi(n-1, y, x, z)
    


n = int(input())

print(2**n - 1)     ## 이동 횟수 최소값

if n <= 20:     ## 20이하일 경우에만 과정 출
    hanoi(n, 1, 2, 3)
