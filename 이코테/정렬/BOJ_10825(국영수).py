import sys
input = sys.stdin.readline

n = int(input())    ##
stu = []

## 0. 학생 점수 입력
for _ in range(n):
    name, kor, eng, math = map(str, input().split())
    stu.append((name, kor, eng, math))


## 정렬(국: 내림, 영: 오름, 수: 내림, 이름: 사전순 증가)
result = sorted(stu, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for s in result:
    print(s[0])