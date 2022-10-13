## 이코테 - 프로그래머스 : 자물쇠와 열쇠
def rotate(a):
    n = len(a)      ## 행 길이
    m = len(a[0])   ## 열 길이

    result = [[0]*n for _ in range(m)]  ## 회전된 결과 저장 리스트
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]

    return result


## 찐 자물쇠 영역이 모두 1인지 확인
def check(new_lock):
    lock_len = len(new_lock) // 3
    
    for i in range(lock_len, lock_len*2):
        for j in range(lock_len, lock_len*2):
            if new_lock[i][j] != 1:     ## 하나라도 값이 1이 아니면 False
                return False
    return True


def solution(key, lock):
    m = len(key)
    n = len(lock)

    ## 3배 확장된 lock
    new_lock = [[0] * (n*3) for _ in range(n*3)]

    ## 확장된 lock 가운데에 기존 lock 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]


    ## 4가지 방향에 대해서 확인
    for _ in range(4):
        key = rotate(key)        ## key 를 90도 회전

        for x in range(n*2):
            for y in range(n*2):

                # 자물쇠에 열쇠 끼워넣기
                # 새로운 잠금영역 해당값 + key에서의 해당 값
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]

                # 검사하기
                if check(new_lock) == True:
                    return True

                ## 자물쇠에서 열쇠 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]

    return False
