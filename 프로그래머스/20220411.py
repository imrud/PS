##def solution(new_id):
##    answer = ''
##    ## 1단계: 대문자-> 소문자
##    new_id = new_id.lower()
##    
##    ## 2단계: ''
##    for s in new_id:
##        if s.isalpha():     ## 알파벳이니?
##            answer += s
##        elif s.isalnum(): ## 숫자니?
##            answer += s
##        elif s in ['-', '_', '.']:      ## 해당되는 특수문자니?
##            answer += s
##
##    ## 3단계: 2번이상 마침표 -> 하나의 마침표로
##    answer = [i for i in answer]
##    for i in range(len(answer)):
##        if answer[i] =='.' and answer[i+1]=='.':
##            del answer[i]
##                
##    return answer
##def solution(arr):
##    answer = []
##    for i in range(len(arr)):
##        if i == 0:
##            print('0: ',i)
##            answer.append(arr[i])
##        elif arr[i] != arr[i-1]:
##            print(i)
##            answer.append(arr[i])
##
##    return answer

##def solution(new_id):
##    answer = ''
##    ## 1단계: 대문자-> 소문자
##    new_id = new_id.lower()
##
##    
##    ## 2단계: 소문자, 숫자, 빼기, ['-', '_', '.'] 이외 문자 제거
##    for s in new_id:
##        if s.isalpha():     ## 알파벳이니?
##            answer += s
##        elif s.isalnum(): ## 숫자니?
##            answer += s
##        elif s in ['-', '_', '.']:      ## 해당되는 특수문자니?
##            answer += s
##
##
##    ## 3단계: 2번이상 마침표 -> 하나의 마침표로
##    tmp = ''
##    for i in answer:
##        if len(tmp) == 0:
##            tmp += i
##        elif i == '.':
##            if i != tmp[-1]:
##                tmp += i
##        else:
##            tmp += i
##     
##    ## 4단계: 문자의 처음, 끝에 마침표 제거
##    if tmp[0] == '.':    ## 처음
##        tmp = tmp [1:]
##    elif tmp[len(tmp)-1] == '.': ## 끝
##        tmp = tmp[:-1]
##    elif tmp[0] == '.' and tmp[len(tmp)-1] == '.':
##        tmp = tmp[1:len(tmp)-1]
##    
##    ## 5단계: 빈 문자열은 'a'로
##    if len(tmp) == 0:
##        tmp += 'a'
##        
##    ## 6단계: 아이디 길이 (16자 이상)
##    if len(tmp) >=16:
##        tmp = tmp[:15]
##        print(tmp)
##        if tmp[-1] == '.':
##            tmp = tmp[:-1]
##
##    ## 7단계 아이디 길이 (2자 이하)
##    if len(tmp) <= 2:
##        while(len(tmp) != 3):
##            tmp += tmp[-1]
##        
##    return tmp
##
##
##print(solution("...!@BaT#*..y.abcdefghijklm"))
##print(solution("=.="))
##def solution(s, n):
##    answer = ''
##    for i in s:
##        if i != ' ':    ## 공백이 아닐 경우
##            if i =='Z':
##                answer += chr(ord("A")+(n-1))
##            elif i == 'z':
##                answer += chr(ord("a")+(n-1))
##            else:
##                answer += chr(ord(i)+n)
##        else:           ## 공백일 경
##            answer += ' '
##    return answer
##
####solution("AaZz", 25)
####solution("a    b", 1)
####solution("a b ", 1)

def solution(s, n):
    answer = ''
    for i in s:
        if i != ' ':
            if 'A' <= i <= 'Z':
                num = ord(i)+n
                print(num)
                if num+> 90:
                    answer += chr(num-26)
                else:
                    answer += chr(num)
            elif 'a' <= i <= 'z':
                num = ord(i)+n
                if num+25 > 122:
                    answer += chr(num-26)
                else:
                    answer += chr(num)
        else:
            answer +=' '
    return answer

