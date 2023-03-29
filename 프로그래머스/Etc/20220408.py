##def solution(s):
##    count = 0
##    for i in s:
##        if i == ['p','P']:
##            count += 1
##        elif i == ['y','Y']:
##            print(i)
##            count -= 1
##            
##    if count == 0:
##        return True
##    else:
##        return False

##def solution(id_list, report, k):
##    id_report = {i:0 for i in id_list}  ## 딕셔너리 이용해서 신고 받은 수 저장
##    print(id_report)
##    for i in report:
##        id_report[i[0]] += 1   ## 신고 받으면 1식 증가 받기
##        print(i)
##        print(id_report[i])
##            
##    
##    answer = [j for j in id_report.values()]
##    return answer

##def solution(board, moves):
##    result = []     ## 뽑은 인형 쌓는 곳
##    count = 0
##    for m in moves:
##        m = m-1
##        for i in range(len(board)):     ## 인형 뽑기 파트
##            if board[i][m] != 0:
##                result.append(board[i][m])
##                board[i][m] = 0     ## 인형 뽑아서 비어있으니 0으로 채워주기
##                break       ## 인형은 해당 위치에서 하나만 뽑을 거다.
##
##            if len(result) != 0:
##                for j in range(len(result)):
##                    if result[i] == result[i+1]:
##                        del result[i]
##                        del result[i+1]
##                        count += 2
##                        break
##    return count

##def solution(board, moves):
##    result = []     ## 뽑은 인형 쌓는 곳
##    count = 0
##    for m in moves:
##        m = m-1
##        for i in range(len(board)):     ## 인형 뽑기 파트
##            if board[i][m] != 0:
##                result.append(board[i][m])
##                board[i][m] = 0     ## 인형 뽑아서 비어있으니 0으로 채워주기
##                break       ## 인형은 해당 위치에서 하나만 뽑을 거다.
##        if len(result) > 1:        
##            if len(result) > 2:
##                if result[-2]==result[-1]:  ## 리스트 마지막 2개 원소가 같다면
##                    result=result[:-2]      ## 슬라이싱해서 result는 그 전까지
##                    count += 2              ## 한 번 터트릴때 2개 씩 터짐
##            else:
##                if result[0] == result[1]:
##                    result = []
##                    count += 2
##    return count
##def solution(absolutes, signs):
##    dict = {}
##    for i in range(len(signs)):
##        dict = {absolutes[i]:signs[i]}
##    
##        
##    answer = 123456789
##    return answer
def solution(n):
    answer = sorted([i for i in str(n)], reverse=True)  ## 리스트에 숫자 넣고 정렬
    return int("".join(answer))    ##join후 정수형으로
