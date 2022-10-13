## 프로그래머스 : 문자열 압축
def solution(s):
    result = []

    ## 문자열 길이 1이면 1 반환
    if len(s) == 1:
        return 1
    
    ## 문자열 1~n까지 나누고 단어 비교
    for i in range(1, len(s)+1):
        b= ''
        cnt = 1     ## 중복 문자열 개수
        tmp = s[:i]  ## 먼저 자르기

        for j in range(i, len(s)+i, i):
            if tmp == s[j:i+j]:     ## 자른 문자열과 같다면
                cnt += 1    ## 카운트 증가

            else:
                if cnt != 1:    ## 앞에서 중복 존재
                    b = b+str(cnt)+tmp
                else:
                    b = b + tmp

                tmp = s[j:j+i]
                cnt = 1         ## 0이면 안
                
        result.append(len(b))
                
                
    return min(result)


print(solution("abcabcdede"))
