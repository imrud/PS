## [CH4] 프로그래머스 : 외벽점검
from itertools import permutations

def solution(n, weak, dist):
    ## 투입할 친구의 최소값 -> 모두가 투입되는 값(최대값)보다 1 큰 값으로 초기화
    answer = len(dist) + 1     
    ## 1. weak의 길이 2배 늘리기 : 원형 -> 일자
    weak_len = len(weak)
    for i in range(weak_len):
        weak.append(weak[i] + n)

    ## 2.dist의 모든 경우의 수 구하기
    dist_p = list(permutations(dist, len(dist)))

    ## 3. 0부터 weak_len - 1까지 start를 이동하면서 찾기
    for start in range(weak_len):
        ## 친구를 나열하는 모든 경우의 수에 대하여 확인
        for p in dist_p:
            count = 1  ## 투입될 친구 수
            ## 해당 친구가 점검할 수 있는 마지막 위치
            position = weak[start] + p[count-1]
            
            ## 시작점부터 모든 취약  지점을 확인
            for i in range(start, start+weak_len):
                ## 점검할 수 있는 위치를 벗어나는 경우
                if position < weak[i]:
                    count += 1      ## new 친구 투입
                    if count > len(dist):   ## 더이상 투입할 친구 없음
                        break
                    ## position 재정비 -> count값 증가로
                    position = weak[i] + p[count-1]
                    
            answer = min(answer, count)     ## 최솟값 계산

    if answer > len(dist):      ## 모든 친구 투입해도 점검X
        print(-1)
        return -1
    print(answer)
    return answer
                        
n = 12
weak = [1, 3, 4, 9, 10]
dist = [3, 5, 7]
solution(n, weak, dist)
