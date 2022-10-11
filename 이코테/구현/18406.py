## 백준 : 18406 - 럭키 스트레이트
import sys
input = sys.stdin.readline

n = input().strip()
n_left = n[:len(n)//2]
n_right = n[len(n)//2:]

l_sum = 0
r_sum = 0
for i in range(len(n_left)):
    l_sum += int(n_left[i])
    r_sum += int(n_right[i])


if l_sum == r_sum:
    print("LUCKY")
else:
    print("READY")
