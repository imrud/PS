answer = 0
def dfs(idx, numbers, target, value):
    global answer

    n = len(numbers)
    if idx == n and value == target:    ## 계산 마지막, target과 같은 경우
        answer += 1
        return
    
    if (idx == n):     ## 계산 마지막, target과 다른 경우
        return

    dfs(idx+1, numbers, target, value+numbers[idx])   ## 다음값 더하기
    dfs(idx+1, numbers, target, value-numbers[idx])   ## 다음값 빼기
        
def solution(numbers, target):
    global answer
    dfs(0, numbers, target, 0)

    return answer
