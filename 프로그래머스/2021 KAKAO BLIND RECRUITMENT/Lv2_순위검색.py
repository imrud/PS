## 프로그래머스 : 순위검색
from itertools import combinations

def solution(info, query):                
    answer = []
    info_dic = {}

    ## 언어/직군/경력/소울푸드 : 딕셔너리 키(key)
    ## 점수 :  딕셔너리 값(value)
    for i in info:
        tmp = i.split()     ## info 분리
        info_key = tmp[:-1]   ## 언어/직군/경력/소울푸드 까지 슬라이싱(whrjs)
        info_value = int(tmp[-1])     ## 점수 / int형으로 점수

        for n in range(5):
            for c in combinations(info_key, n):## (0,1,2,3)에서 n개 조합
                
                tmp_key = ''.join(c)    ## 조합을 문자열로 -> key
                
                if tmp_key in info_dic:         ## 존재하면 값 추가
                    info_dic[tmp_key].append(info_value)
                else:       ## 없으면 새로운 키,value 넣어주기
                    info_dic[tmp_key] = [info_value]


    print(info_dic)
    ## 이분탐색 위한 정렬
    for k in info_dic.keys():
        info_dic[k].sort()      ## value(score)를 오름차순으로 정렬
    print('\n')
    print(info_dic)

    ## 쿼리 부수기
    for qu in query:
        q = qu.split(' ')
        q_score = int(q[-1])        ## 점수만 따로 빼기
        q_query = q[:-1]        ## 조건 슬라이싱

        while 'and' in q_query:     ## 조건문 내 'and' 흔적 지우기
            q_query.remove('and')
        while '-' in q_query:       ## 조건문 내 '_' 있으면 흔적 지우기
            q_query.remove('-')

        q_query = ''.join(q_query)  ## 조건 배열을 문자열로 만들기

        if q_query in info_dic:
            scores = info_dic[q_query]      #3 해당 조건의 value 가져오기

            ## 해당 쿼리의 값이 여러개 있을수 있음
            if len(scores) > 0:

                ## 이분탐색 들어가기
                start, end = 0, len(scores)
                while start < end:
                    mid = (start + end) // 2
                    if scores[mid] >= q_score:
                        end = mid
                    else:
                        start = mid + 1     # 그 다음값하고 비교하러 가기
                answer.append(len(scores) - start)

        else:
            answer.append(0)
            
    return answer
