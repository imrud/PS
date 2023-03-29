def solution(survey, choices):
    answer =''
    cDict = {'R':0, 'T':0,'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}   ## 라이언, 튜브형
##    chracter2 = {'C':0, 'F':0}   ## 콘형, 프로도형
##    chracter3 = {'J':0, 'M':0}   ## 제이지형, 무지형
##    chracter4 = {'A':0, 'N':0}   ## 어피치형, 네오형
    sDict = {1:3, 2:2, 3:1, 4:0, 5:1, 6:2, 7:3}     ## choices에 따른 점수 딕셔너리로

    ##점수 매기기
    for i in range(len(survey)):
        if survey[i][0] in ['R', 'T']:
            if choices[i] < 4:      ## survey[i]에서 첫번째 캐리턱에 대한답(비동의)
                chracter1[survey[i][0]] += sDict[choices[i]]   ## 점수부여
            else:
                chracter1[survey[i][1]] += sDict[choices[i]]   ## 점수부여
        elif survey[i][0] in ['C', 'F']:
            if choices[i] < 4:      ## survey[i]에서 첫번째 캐리턱에 대한답(비동의)
                chracter1[survey[i][0]] += sDict[choices[i]]   ## 점수부여
            else:
                chracter1[survey[i][1]] += sDict[choices[i]]   ## 점수부여
        elif survey[i][0] in ['J', 'M']:
            if choices[i] < 4:      ## survey[i]에서 첫번째 캐리턱에 대한답(비동의)
                chracter1[survey[i][0]] += sDict[choices[i]]   ## 점수부여
            else:
                chracter1[survey[i][1]] += sDict[choices[i]]   ## 점수부여
        else:
            if choices[i] < 4:      ## survey[i]에서 첫번째 캐리턱에 대한답(비동의)
                chracter1[survey[i][0]] += sDict[choices[i]]   ## 점수부여
            else:
                chracter1[survey[i][1]] += sDict[choices[i]]   ## 점수부여

    print(chracter1)
    ## 점수 판단하기
    dList = list(zip(chracter1.keys(), chracter1.values()))
    for i in range(0, len(dList), 2):
        print(i, dList[i])
        if dList[i][1] >= dList[i+1][1]:
            answer += dList[i][0]
        else:
            answer += dList[i+1][0]
            
##    answer += max(chracter1, key=chracter1.get)
##    answer += max(chracter2, key=chracter2.get)
##    answer += max(chracter3, key=chracter3.get)
##    answer += max(chracter4, key=chracter4.get)

    return answer
