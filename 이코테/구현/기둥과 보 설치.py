## [CH4] 프로그래머스 : 기둥과 보 설치
def check(answer):
    for x, y, stuff in answer:      ## 위치, 구조물 종류
        
        if stuff == 0:    ## 기둥일경우
            ## 바닥 / 보의 한 쪽 끝부분 위 / 다른 기둥 위
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False


        elif stuff == 1:  ## 보일 경우
            ## 한 쪽 끝부분이 기둥 위 / 양쪽 끝 부분이 보인 경우 
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False

    return True

def solution(n, build_frame):
    answer = []
    for fr in build_frame:
        x, y, stuff, operate = fr    ## 위치(x,y), 구조물종류, 설치여부

        if operate == 1:        ## 설치하는 경우
            answer.append([x, y, stuff])
            if not check(answer):
                answer.remove([x, y, stuff])

        elif operate == 0:    ## 삭제하는 경우
            answer.remove([x, y, stuff])
            if not check(answer):
                answer.append([x, y, stuff])


    answer.sort()
    print(answer)
    return sorted(answer)


n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]

solution(n, build_frame)
