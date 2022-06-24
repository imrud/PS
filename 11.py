#01
##n, m = map(int, input().split())
##cl = list(map(int, input().split()))
##cl.sort(reverse=True)    ## 내림차순으로 정렬
##sum = 0
##m = m-cl[0]     ## 먼저 입력받은 수 중에서 최대값 빼기
##nl = []
##for i in range(1, n):
##    if cl[i] <= m:
##        nl.append(cl[i])
##nl.sort(reverse = True)
##print(cl[0]+nl[0])
## 인터넷
##n, m = map(int, input().split())
##cl = list(map(int, input().split()))
##result = 0
##
##for i in range(n):              ## 처음 선택
##    for j in range(i+1, n):     ## 두 번째 선택
##        for k in range(j+1, n):     ## 세 번째 선택
##            if cl[i]+cl[j]+cl[k] > m:   ## 세 카드의 합이 m보다 클 경우
##                continue
##            else:
##                result = max(result, cl[i]+cl[j]+cl[k]) 
##                ## 작은 값들은 result에 저장하면서 계속 최대값 갱신
##print(result)
## python 라이브러리 사용
##from itertools import combinations
##
##n, m = map(int, input().split())         ## n,m입력
##cl = list(map(int, input().split()))     ## n개의 수를 리스트로 입력받기
##result = 0
##
##for cn in combinations(cl, 3):
##    if result < sum(cn) <= m:
##        result = sum(cn)            ## 범위안에 들면 result에 값 저장하면서 계속 비교하기
##        
##print(result)


#02
##n = int(input())
##
##for 
    



#03
##import sys
##pl = []     ## 입력받을 (키, 몸무게) 저장할 리스트
##
###입력
##for i in range(int(sys.stdin.readline())):
##    height, weight = map(int, sys.stdin.readline().split())
##    pl.append((height, weight))
##
### for문
##for i in range(len(pl)):
##    count = 0
##    for j in range(len(pl)):
##        if pl[i][0] < pl[j][0]:
##            if pl[i][1] < pl[j][1]:
##                count += 1
##    print(count+1, end=" ")     ## 본인등수는 자신보다 더 큰 덩치수+1
               


#04
##import sys
##m, n = map(int, sys.stdin.readline().split())
##black = 32
##white = 32
##for i in range(m):      # 행
##    color = sys.stdin.readline().strip()  ##strip() 사용해서 개행문자처리
##    for j in range(n):  # 열
##        if color[j] == 'W': 
##            white -= 1
##        else:
##            black -= 1
##
##print(white+black)
## 인터넷
import sys
## 0.입력받기
n , m = map(int, sys.stdin.readline().split())
board = []
for _ in range(n):
    board.append(int(sys.stdin.readline()))

## 1.체스판 자르기
for i in range(



#05
##import sys
##n = int(sys.stdin.readline())
##fn = 666
##
##while n != 0:
##    if '666' in str(fn):
##        n = n-1
##        if n == 0:
##            break
##    fn = fn+1
##print(fn)

