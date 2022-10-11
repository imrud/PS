## 백준 : 1914
import sys
input = sys.stdin.readline

## (원반의 개수, 현재 기둥, 도착 기둥, 보조 기둥)
def hanoi(n, from_peg, to_peg, aux_peg):
    if n == 1:
        print(from_peg, to_peg)
        return

    ## 가장 큰 원반 제외한 원반들을, 보조기둥으로 옮기기
    hanoi(n-1, from_peg, aux_peg, to_peg)

    ## 가장 큰 원반 옮기
    print(from_peg, to_peg)

    #3 보조기둥에 옮겼던 원반들을 목적지(to_peg)로 옮기
    hanoi(n-1, aux_peg, to_peg, from_peg)
    


n = int(input())

print(2**n - 1)     ## 이동 횟수 최소값(= 메르센 수)

if n <= 20:     ## 20이하일 경우에만 과정 출력
    hanoi(n, 1, 3, 2)
