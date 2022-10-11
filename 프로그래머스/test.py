##def solution(n):
##    ## 홀수에는 수, 짝수에는 박
##    
##    sstr = []
##    while (n != 0):
##        if n%2 != 0:
##            sstr.append("수")
##        else:
##            sstr.append("박")
##    answer = str("".joint(sstr))
##    return answer
##
##print(solution(3))


##def solution(numbers, hand):
##    answer =''
##
##    ## 키패드 숫자 위치를 좌표로!
##    kdict = {1:[0,0], 2:[0,1], 3:[0,2],
##             4:[1,0], 5:[1,1], 6:[1,2],
##             7:[2,0], 8:[2,1], 9:[2,2],
##             '*':[3, 0], 0:[3, 1], '#':[3, 2]}
##    curR = '*'      ## 처음 오른손 위치
##    curL = '#'      ## 처음 왼손 위치
##
##    for i in numbers:
##        if i in [1, 4, 7]:      ##1,4,7은 왼손
##            answer += 'L'
##            curL = i
##        elif i in [3, 6, 9]:    ##3,6,9는 오른쪽
##            answer += 'R'
##            curR = i
##        else:
##            laxis = kdict[curL]   ## 현재 왼손에 해당하는 좌표
##            raxis = kdict[curR]   ## 현재 오른손에 해당하는 좌표
##
##            ## 거리 절댓값 -> (x1-nx)+(y1-ny)
##            ld = abs(laxis[0]-kdict[i][0]) + abs(laxis[1]-kdict[i][1]) ## 오른손 거리
##            rd = abs(raxis[0]-kdict[i][0]) + abs(raxis[1]-kdict[i][1]) ## 왼쪽 거리
##
##            if rd < ld:     ## 오른손이 더 가까움
##                answer += 'R'
##                curR = i 
##            elif rd > ld:     ## 왼손이 더 가까움
##                answer += 'L'
##                curL = i
##            else:                   ## 거리가 같을때
##                if hand == "right":
##                    answer += 'R'
##                    curR = i
##                else:
##                    answer += 'L'
##                    curL = i
##
##    
##    return answer


##def solution(a, b):
##    answer = 0
##    n = len(a)
##    for i in range(n):
##        answer += a[i][n-i] * b[i][n-i]
##    return answer

##def solution(seoul):
##    x = 0           # 김서방 위치
##    while True:
##        print(x)
##        print(seoul[x])
##        if seoul[x] == "kim":
##            break
##        print(x)
##        x += 1
##    s = "김서방은 "+str(x)+"에 있다"
##    return s
##def solution(x):
##    sum = 0
##    t = x
##    for i in range(len(str(x))-1, 0, -1):
##        sum = sum+(x//(10**i))
##        x = x%(10**i)
##    print(sum)
##    if x%sum==0:
##        return True
##    else:
##        return False


def solution(seoul):
    x = 0           # 김서방 위치
    for i in seoul:
        if i == "kim":
            break
        x += 1
    result = "김서방은 "+str(x)+"에 있다"
    return result
