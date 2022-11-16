T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    score = list(map(int, input().split()))

    cnt = [0] * 101  ## 0점부터 100점까지
    for i in score:
        cnt[i] += 1


    fre_idx = 0     ## 최대 빈도 점수
    fre_num = 0     ## 최대 빈도수
    for i in range(101):
        if cnt[i] >= fre_num:
            fre_num = cnt[i]
            max_idx = i

    ## 실패
    # fre_score = 0       ## 최대 빈도수의 값
    # for i in range(101):
    #     if score.count(i) == 0:
    #         continue
    #     elif score.count(i) >= score.count(fre_score):    ## 현재 최대 빈도수보다 크거나 같은 경우 -> 더 큰 점수로 갱신
    #         fre_score = score[i]


    print('#{} {}'.format(test_case, max_idx))
