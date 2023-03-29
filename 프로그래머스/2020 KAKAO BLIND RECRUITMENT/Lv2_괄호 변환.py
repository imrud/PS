## 2) u, v 분리
def divide(p):
    op = 0
    cp = 0

    for i in range(len(p)):
        if p[i] == '(':
            op += 1
        else:
            cp += 1
        if op == cp:    ## '('와 ')'의 개수가 같아지는 바로 그 순간
            return p[:i+1], p[i+1:]

## 3) 문자열 u에 대해 올바른 괄호 문자열 확인
def isChecked(u):
    stack = []
    
    for p in u:
        if p == '(':
            stack.append(p)
        else:
            if not stack:       ## 갯수가 안 맞음
                return False
            stack.pop()
            
    return True

def solution(p):
    ## 1. 입력이 빈 문자열 ->  빈 무자열 반환
    if not p:
        return ""

    ## 2. 문자열을 u, v로 나누기
    u, v = divide(p)

    #answer = ''
    ## 3. 균형잡힌 문자열 결과
    if isChecked(u):    #균형 잡혔다면 v에 대해 첨부터 진행
        return u + solution(v)

    ## 4. 반복
    else:
        answer = '('
        answer += solution(v)
        answer += ')'

        for p in u[1:-1]:
            if p == '(':
                answer += ')'
            else:
                answer += '('
        return answer
        
