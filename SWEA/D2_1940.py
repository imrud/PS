## 1940
T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    speed = 0       ## 초기 속도
    distance = 0    ## 이동거리

    for _ in range(n):
        command = list(map(int, input().split()))

        if command[0] == 1:   ## 커맨드 =1, 가속
            speed += command[1]
            
        elif command[0] == 2:     ## 커맨드 = 2, 감속
            if speed > command[1]:
                speed -= command[1]
            else:
                speed = 0
        distance += speed

    print('#{} {}'.format(test_case, distance))
