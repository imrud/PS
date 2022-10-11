def solution(dartResult):
    answer = 0
    tmp =''
    dr = []
    for i in range(len(dartResult)):
        if i == 0:
            tmp +=dartResult[i]
        else:   
            if dartResult[i].isdigit():
                if dartResult[i] == '0' and dartResult[i-1] == '1':
                    tmp += dartResult[i]
                else:
                    dr.append(tmp)
                    tmp = ''
                    tmp += dartResult[i]          
            else:
                tmp += dartResult[i]
    dr.append(tmp)
    print(dr)

    ## 인덱스 -> 점수:0, 보너스:1, 옵션:2    
    #점수 계산하기
    pre=0
    for i in range(len(dr)):
        if len(dr[i]) == 2 or (len(dr[i]==3) and (dr[i][1] == 0)):
            if len(dr[i]) == 2:
                if dr[i][1] == 'S':
                    pre = int(dr[i][0])*1
                    answer += pre
                elif dr[i][1] == 'D':
                    pre = int(dr[i][0])**2
                    answer += pre
                else:
                    pre = int(dr[i][0])**3
                    answer += pre
            else:
                if dr[i][2] == 'S':
                    pre = 10*1
                    answer += pre
                elif dr[i][2] == 'D':
                    pre = 10**2
                    answer += pre
                else:
                    pre = 10**3
                    answer += pre
            
        else: 
            if dr[i][2] == '*':     ##스타상 현재값, 이전값 2배
                if dr[i][1] == 'S':
                    answer += (int(dr[i][0])*1)*2+pre
                    pre = answer
                elif dr[i][1] == 'D':
                    answer += (int(dr[i][0])**2)*2+pre
                    pre = answer
                else:
                    answer += (int(dr[i][0])**3)*2+pre
                    pre = answer
            else:                   ## 아차상 현재값-하기
                if dr[i][1] == 'S':
                    answer += (-1)*int(dr[i][0])*1
                    pre = answer
                elif dr[i][1] == 'D':
                    answer += (-1)*int(dr[i][0])**2
                    pre = answer
                else:
                    answer += (-1)*int(dr[i][0])**3
                    pre = answer 
                
    return answer
