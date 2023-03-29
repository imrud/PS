##def solution(n, lost, reserve):
##
##    answer = n - (len(lost)+len(reserve))  ## 남은 학생수
##    print("1: ", answer)        
##    for i in lost:
##        if i in reserve:
##            reserve.remove(i)
##            lost.remove(i)
##            answer += 1
##            print("i: ", answer)        
##        elif (i-1) in reserve:
##            reserve.remove(i-1)
##            lost.remove(i)
##            answer += 2     ## 체육 수업 들을 수 있는 사람 한 명 추가
##            print("i-1: ", answer)  
##        elif (i+1) in reserve:
##            reserve.remove(i+1)
##            lost.remove(i)
##            answer += 2     ## 체육 수업 들을 수 있는 사람 한 명 추가
##            print("i+1: ", answer)  
##
##    return answer

def solution(dartResult):
    answer = 0
    tmp =''
    dr = []
    for i in range(len(dartResult)):
        
        if i == 0:
            tmp +=dartResult[i]
        else:   
            if dartResult[i].isdigit():
                print(dartResult[i])
                if dartResult[i] == '0' and dartResult[i-1] == '1':
                    tmp += dartResult[i]
                    print(tmp)
                else:
                    print(i)
                    dr.append(tmp)
                    tmp = ''
                    tmp += dartResult[i]          
            else:
                tmp += dartResult[i]
    dr.append(tmp)
    print(dr)


    #점수 계산하기
    for i in range(len(dr)):
        if len(dr[i]) == 3:
            if dr[i][1] == 'S':
                answer += int(dr[i][0])*1
                if dr[i][2] == '*':
                    if i==0:        ## 첫번째 기회에서 나온경우
                        answer += int(dr[i][0])*2
                    else:
                        answer += int(dr[i-1][0])*2
                elif dr[i][2] == '#':
                    if i==0:        ## 첫번째 기회에서 나온경우
                        answer += -int(dr[i][0])
                    else:
                        answer += -int(dr[i-1][0])
            elif dr[i][1] == 'D':
                answer += int(dr[i][0])**2
                if dr[i][2] == '*':
                    if i==0:        ## 첫번째 기회에서 나온경우
                        answer += int(dr[i][0])*2
                    else:
                        answer += int(dr[i-1][0])*2
                elif dr[i][2] == '#':
                    if i==0:        ## 첫번째 기회에서 나온경우
                        answer += -int(dr[i][0])
                    else:
                        answer += -int(dr[i-1][0])
            else:
                answer += int(dr[i][0])**3
                if dr[i][2] == '*':
                    if i==0:        ## 첫번째 기회에서 나온경우
                        answer += int(dr[i][0])*2
                    else:
                        answer += int(dr[i-1][0])*2
                elif dr[i][2] == '#':
                    if i==0:        ## 첫번째 기회에서 나온경우
                        answer += -int(dr[i][0])
                    else:
                        answer += -int(dr[i-1][0])
            
        else:
            if dr[i][1] == 'S':
                answer += int(dr[i][0])*1
            elif dr[i][1] == 'D':
                answer += int(dr[i][0])**2
            else:
                answer += int(dr[i][0])**3
            
            
    return answer
