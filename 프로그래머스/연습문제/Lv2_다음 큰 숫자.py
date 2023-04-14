def solution(n):
    answer = 0
    tmp = bin(n)
    tmp = tmp[2:]
    cnt_n = tmp.count('1')  ## 1의 개수 세기
    t = n

    while True:
        t += 1
        tb = bin(t)[2:]
        if tb.count('1') == cnt_n:
            answer = t
            break


    return answer

print(solution(15))
