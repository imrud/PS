## [CH4] 실전문제 - 왕실의 나이트
import sys

input = sys.stdin.readline

n = input()
row = int(n[1])     ## 행
col = int(ord(n[0])) - int(ord('a')) +1     ## 열(숫자로 바꾸기)

## 이동 가능한 8가지 방향
steps = [(-2, -1), (-1, -2), (1, -2),
         (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]


## 위치 확인하기
count = 0
for step in steps:
    nr = row + step[0]
    nc = col + step[1]

    ## 범위 확인하기 (인덱스 1부터 시작)
    if 1 <= nr <= 8 and 1 <= nc <= 8:
        count += 1


print(count)


