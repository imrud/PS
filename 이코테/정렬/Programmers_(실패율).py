def solution(N, stages):
    fail_dict = {}
    user_len = len(stages)

    for i in range(1, N+1):
        if user_len != 0:
            cnt = stages.count(i)
            fail_dict[i] = cnt / user_len
            user_len -= cnt
        else:
            fail_dict[i] = 0

    ## 정렬하기
    #print(tmp)
    result = sorted(fail_dict, key=lambda x: fail_dict[x], reverse=True)

    return result


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))

## 실패문제풀이
# for i in range(N):
#         fail_dict[i+1] = stages.count(i+1)
#     user_len = len(stages)
#     #print(fail_dict)
#     tmp = {}
#
#     ## 실패율 구하기
#     for i in fail_dict:
#
#         if i == 1:
#             tmp[i] = fail_dict[i]/user_len
#         else:
#             user_len = user_len - fail_dict[i-1]
#
#             tmp[i] = fail_dict[i] / user_len

#### 예전 문제풀이
# def solution(N, stages):
#     ##player = len(stages)     ## 전체 사용자 수
#     fail_rate = {}  ## 스테이지에 따른 실패율을 딕셔너리로 저장
#     for i in range(1, N + 1):  ## 스테이지는 1~n+1단계까지 존재
#         if i in stages:
#             rp = 0  ## 스테이지 도달한 사용자
#             np = 0  ## 도달했지만 성공 아직 못한 사용자
#             for j in stages:
#                 if j >= i:  ## 도달한 사람 수
#                     rp += 1
#                 if j == i:  ## 해당 스테이지 아직 클리어 못한 사용자
#                     np += 1
#             fail_rate[i] = np / rp
#         else:
#             fail_rate[i] = 0  ## 실패율이 0
#
#     return sorted(fail_rate, key=fail_rate.get, reverse=True)
