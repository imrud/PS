## 백준 : 10989
import sys
input = sys.stdin.readline

n = int(input())
nums = [0]*10001        ## 인덱스는 0부터 시작하니 10001개로

for _ in range(n):
    ## 입력받은 수를 인덱스로 사용
    ## 값은 값 입력 받을 시, 해당 인덱스의 value 1씩 증가
    nums[int(input())] += 1


for i in range(10001):
    ## 인덱스 값이 존재하면
    if nums[i] != 0:
        ## 해당 인덱스의 value만큼 for문 돌려서
        ## 인덱스를 출력
        for j in range(nums[i]):    
            print(i)
