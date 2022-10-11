## 백준 : 연산자 끼워넣기 - 14888
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))              ## 수
add, sub, mul, div = map(int, input().split())      ## 연산자


## 최댓값, 최솟값 초기화
max_value = -1e9
min_value = 1e9


## dfs 이용(실행 횟수, 값)
def dfs(i, now):
    ## 전역변수 설정
    global max_value, min_value, add, sub, mul, div

    
    if i == n:            # 연산 다 수행했을 때
        max_value = max(max_value, now)
        min_value = min(min_value, now)


    else:
        if add > 0:
            add -= 1        ## 횟수 차감
            dfs(i+1, now+nums[i])
            add += 1
            
        if sub > 0:
            sub -= 1        ## 횟수 차감
            dfs(i+1, now - nums[i])
            sub += 1
            
        if mul > 0:
            mul -= 1        ## 횟수 차감
            dfs(i+1, now*nums[i])
            mul += 1
            
        if div > 0:
            div -= 1        ## 횟수 차감
            dfs(i+1, int(now/nums[i]))
            div += 1
            
        
        


## 메서드 호출 (연산 시행 횟수, 값)
dfs(1, nums[0])

## 최댓값, 최솟값 출력
print(max_value)
print(min_value)
