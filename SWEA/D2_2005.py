T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    res = []

    for i in range(n):
        tmp = []
        for j in range(i+1):
            if 0 < j < i:
                tmp.append(res[i - 1][j - 1] + res[i - 1][j])
            else:
                tmp.append(1)
        res.append(tmp)

    print('#{}'.format(test_case))
    for i in range(n):
        for j in res[i]:
            print(j, end=' ')
        print()



