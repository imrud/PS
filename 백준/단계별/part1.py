#01
##n, k = map(int, input().split())
##dvisior = []
####for i in range(1, (n//2)+1):
####    if n % i == 0:
####        dvisior.append(i)
####        dvisior.append(n//i)
##
##for i in range(1, n+1):
##    if n % i == 0:
##        dvisior.append(i)
##        
####dl = list(set(dvisior))
####dvisior = set(dvisior)
####dvisior.sort()
##
##if len(dvisior) >= k:
##    print(dvisior[k-1])
##    
##else:
##    print(0)

#02이진수
##import sys

#1. 입력받기
##t = int(sys.stdin.readline())
##nlist = list(map(int, sys.stdin.readline().split()))
##
###2. 2로 나눠서 나머지 저장하기
##for n in nlist:
##    blist = []   ## 나머지 저장
##    while True: 
##        rn = n%2    ## 나머지(1아니면 0)
##        n = n//2    ## 몫(2로 나눠서 계속 새로운 n값 갱신)
##        if n == 0:         ## 몫이 0이면 while문 종료
##            blist.append(1)
##            break
##        else:
##            blist.append(rn)
##    for i in range(len(blist)):
##        if blist[i] == 1:
##            print(i, end=" ")
##    print()

###인터넷 참고-맞음
##for _ in range(int(sys.stdin.readline())):
##    n = int(sys.stdin.readline())
##
##    count = 0
##    while n != 0:
##        if n%2 == 1:
##            print(count, end=" ")    ## 나머지 1이면 바로 출력
##        n = n // 2
##        count += 1  ## 한 번씩 거칠때마다 count값 1씩 증가
##    print()


###03.최소,최대
##import sys
##n = int(sys.stdin.readline())
##nlist = list(map(int, sys.stdin.readline().split()))
##
###최대, 최소 기본 설정
##m, M = nlist[0], nlist[0]
##
###정렬하기
##for num in nlist:
##    if m >= num:
##        m = num
##    if M <= num:
##        M = num
##            
##print(m, M)    
#####python적
######print(min(nlist), max(nlist))


###04.지능형 기차2
##import sys
##
##sp = 0   ## 탄 사람수
##mp = 0   ##최대 사람
##for i in range(10):
##    gof, gon = map(int, sys.stdin.readline().split())   ##gof: 내, gon:탄
##    sp = sp-gof+gon
##    if sp > mp:
##        mp = sp
##print(mp)

    

#05. 피보나치 수5


#####06.일곱 난쟁이
##import sys
##nan = [int(sys.stdin.readline().strip()) for i in range(9)]
####nan.sort()
####for a in range(9):
####    for b in range(a, 9):
####        for c in range(b, 9):
####            for d in range(c, 9):
####                for e in range(d, 9):
####                    for f in range(e, 9):
####                        for g in range(f, 9):
####                            if nan[a]+nan[b]+nan[c]+nan[d]+nan[e]+nan[f]+nan[g] == 100:
####                                print(nan[a])
####                                print(nan[b])
####                                print(nan[c])
####                                print(nan[d])
####                                print(nan[e])
####                                print(nan[f])
####                                print(nan[g])
####                                break
##asum = sum(nan)  ## 9난쟁이 합
##for i in range(9):
##    for j in range(i+1, 9):
##        if asum - (nan[i]+nan[j]) == 100:
##            fn1, fn2 = nan[i], nan[j]
##            break
##
##nan.remove(fn1)
##nan.remove(fn2)
##nan.sort()
##
##for i in nan:
##    print(i)


##07. 최대공약수와 최소공배수 (🥈실버 5티어)
##import sys
##
##n, m = map(int, sys.stdin.readline().split())
##nlist = []
##for i in range(2, n):
##    if n % i == 0:
##        nlist.append(i)
##for j in range(2, m+1):
##    if m % i==0:
##        nlist.append(j)
##result = list(set(nlist))
##result.sort()
##k = len(result)
##print(result[0], result[k-1])
##    


##08. N번째 큰 수 (🥈실버 5티어)
import sys
for _ in range(int(sys.stdin.readline(),split()):
               


##09. 소수 찾기 (🥈실버 4티어)



##10. 쉽게 푸는 문제 (🥈실버 4티어)


##11. 소수 (🥈실버 4티어)





            

                                
        
