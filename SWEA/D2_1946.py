T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    res=''
    for _ in range(n):
        alpha, cnt = input().split()
        res += alpha*int(cnt)

    print('#{}'.format(test_case))
    ## 인터넷 풀이
    #for i in range(0, len(res), 10):
    #    print(res[i:i + 10])

    ## 내 풀이
    if len(res)%10 == 0:
        t = len(res) // 10
    else:
        t = (len(res) // 10) + 1
    for i in range(t):
        print(res[:10])
        res = res[10:len(res)]
