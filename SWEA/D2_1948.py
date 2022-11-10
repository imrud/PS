## 1948.날짜 계산기
T = int(input())

mon = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for test_case in range(1, T + 1):
    m1, d1, m2, d2 = map(int, input().split())

    res = 0
    if m1 == m2:
        res = d2-d1+1
    else:
        res += (mon[m1] - d1)+1 + d2
    
    ## 그 사이기간 날짜
    for i in range(m1+1, m2):
        res += mon[i]
    

    print('#{} {}'.format(test_case, res))
    
    
