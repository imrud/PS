## 백준 : 11729
import sys
input = sys.stdin.readline

## 원 개수, 출발지 기둥, 목적지 기둥, 보조 기둥
def hanoi(n, from_col, to_col, ass_col):
    if n == 1:
        print(from_col, to_col)
        return

    ## n-1개까지 보조 기둥으로 옮기기(가장 큰 기둥은 제외) // 출발지 -> 보조
    hanoi(n-1, from_col, ass_col, to_col)

    ## 가장 큰 원반은 목적지로  옮기기 // 출발지 -> 목적지
    print(from_col, to_col)

    ## 보조 기둥에 옮겨 놓은 n-1개 원판을, 목적지로// 보조 -> 목적지
    hanoi(n-1, ass_col, to_col, from_col)


n = int(input())

print(2**n - 1)
hanoi(n, 1, 3, 2)


## -----매개변수 3개 버전-----

#### 원판 개수, 출발지, 도착지
##def hanoi(n, start, end):
##    if n == 1:
##        print(start, end)
##        return
##
##    ## 6-start-end : 1번, 3번 막대 제외한 2번막대 의미)
##    hanoi(n-1, start, 6-start-end)  ## 1단계
##    print(start, end)               ## 2단계
##    hanoi(n-1, 6-start-end, end)    ## 3단계
##    
##
##n = int(input())
##
##print(2**n - 1)
##hanoi(n, 1, 3)
