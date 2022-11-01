## 성적이 낮은 순서로 학생 출력하기
import sys
input = sys.stdin.readline
n = int(input())

stu = []
for _ in range(n):
    data = input().split()
    stu.append((data[0], int(data[1])))


stu.sort(key = lambda x: x[1])

for i in stu:
    print(i[0], end= ' ')
