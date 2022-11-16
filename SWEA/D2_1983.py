T = int(input())
grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D']
for test_case in range(1, T + 1):
    N, K = map(int, input().split())

    stu = []
    for _ in range(N):
        mid, final, work = map(int, input().split())
        stu.append((mid*0.35) + (final*0.45) + (work*0.20))

    tmp = stu[K-1]

    ## 내림차순으로 정렬
    stu.sort(reverse=True)
    div = N // 10
    res = stu.index(tmp) // div

    print('#{} {}'.format(test_case, grade[res]))
