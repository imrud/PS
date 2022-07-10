#01
##n = int(input())
##nl = list(map(int, input().split()))
##sum = 0
##
##for i in range(n):
##    count = 0
##    for j in range(2, nl[i]):        ##1과 n[i](자기자신)빼고 나누어져야함.
##        if nl[i]%j != 0:
##            count += 1
##        else:
##            count -= 0
##    if count > 0:
##        sum += 1
##
##print(sum)
#### 인터넷
##n = int(input())
##nl = list(map(int, input().split()))
##sum = 0
##
##for i in nl:
##    count = 0
##    if (i == 1):  # 1은 소수가 아니기 때문에
##        continue
##    for j in range(2, i+1):        ##1과 자기자신(i) 빼고 나누어지면 소수X
##        if i%j == 0:
##            count += 1
##    if count == 1:  # i%i==0 이경우가 있기때문에 소수더라도 count=1
##        sum += 1
##
##print(sum)   


##02
##m = int(input())
##n = int(input())
##nl = []
##
####for i in range(m, n+1):
####    count = 0    ## 다른 수 체크 할 때마다 count 초기화
####    if( i == 1):
####        continue
####    for j in range(2, i):
####        if i%j == 0:    ## 1, 자기자신(i) 제외해도 다른수로 나누어짐 ->  소수X
####            count += 1
####    if count == 0:      ## 소수이면 리스트에 추가
####        nl.append(i)
####if len(nl) == 0:
####    print(-1)
####else:
####    print(sum(nl))  ## sum()함수 이용해서 리스트 합 구하기
####    print(min(nl))
#### 인터넷
##for i in range(m, n+1):
##    count = 0    ## 다른 수 체크 할 때마다 count 초기화
##    if i > 1:
##        for j in range(2, i):
##            if i%j == 0:    ## 1, 자기자신(i) 제외해도 다른수로 나누어짐 ->  소수X
##                count += 1
##                break   ## 소수 아니니까 굳이 더 계산 안해도 됨
##        if count == 0:      ## 소수이면 리스트에 추가
##            nl.append(i)
##
##if len(nl) > 0:
##    print(sum(nl))  ## sum()함수 이용해서 리스트 합 구하기
##    print(min(nl))
##else:
##    print(-1)


#03
##n = int(input())
##snl = []  ## 소인수 분해 결과 담을 리스트
##
##def sn(n):
##    if n != 1: # n인 1이 아닌 경우에만 실행
##        for i in range(2, n):
##            if n % i == 0:
##                n = n//i  # n에 몫 저장
##                if n!=1:
##                    snl.append(i)  # 해당 i(나누어지는 수) 추가하기
##                    sn(n)
##            else:
##                continue
##                
##sn(n)            
##if len(snl) > 0:
##    for i in snl:
##        print(i)

###인터넷(while)
##n = int(input())
##for i in range(2, n+1):
##    if n % i ==0:  ## 나누어 떨어질때
##        while n % i ==0:
##            print(i)
##            n = n/i
    


#04
## 시간초
##m, n = map(int, input().split())
##for i in range(m, n+1):
##    count = 0    ## 다른 수 체크 할 때마다 count 초기화
##    if i > 1:
##        for j in range(2, i+1):
##            if i%j == 0:    ## 1, 자기자신(i) 제외해도 다른수로 나누어짐 ->  소수X
##                count += 1
##        if count == 1:      ## 소수이면 출력
##            print(i)
## 에라토스테네스의 
##def isPrime(num):
##    if num == 1:    ## m =1인 경우
##        return False    
##    else:
##        for i in range(2, int(num**0.5) + 1):
##            if num % i == 0:
##                return False
##        return True
## 
## 
##m, n = map(int, input().split())
## 
##for i in range(m, n + 1):
##    if isPrime(i):
##        print(i)


    
#05
##while True:
##    n = int(input())
##    if n == 0:
##        break   ## 0입력받으면 while문 종료
##    
##    sum = 0
##    for i in range(n, 2*n+1):
##        count = 0
##        if (i==1):
##            continue
##        for j in range(2, i+1):
##            if i%j == 0:
##                count += 1
##        if count == 1:
##            sum += 1
##    print(sum)
##    
#### 인터넷 -> 에라토스테네스의 체 이용// 에라토스테네스 공부하기
##def isPrime(num):
##    sieve = [True]*num
##    for i in range(2, int(num**0.5)+1):
##        if sieve[i] == True:
##            for j in range(i+i, num, i):
##                sieve[j] = False
##    return [i for i in range(2, num) if sieve[i] == True]
##
##while True:
##    n = int(input())
##    if n == 0:
##        break   ## 0입력받으면 while문 종료
##    nl = isPrime(2*n+1)
##    print(len([i for i in nl if i > n]))


###06
##def isPrime(n):
##    nl = []
##    for i in range(2, n):
##        if not n% i:
##            break
##        else:
##            nl.append(i)
##    return nl
##
##t = int(input())
##for i in range(t):
##    num = int(input())
##    nl = isPrime(num).sort(reverse=True)
##    rl = []
##    for i in nl.:
##        if num != 0
##        
##        num
##        num - i
##    
##num = int(input())
##if num > 3:
##    nl = isPrime(num)
##    print(nl)
##### 인터넷
##import math
##def isPrime(n):     ## n이하의 숫자에서 소수 판별
##    for i in range(2, int(math.sqrt(n))+1):
##        if n % i == 0:
##            return False    ## 1, 자기자신 외에 나누어지면 소수X
##    return True
##
##t = int(input())         ## 테스트 케이스 개수
##for _ in range(t):
##    n = int(input())     ## 짝수n 입력받기
##    
##    a = int(n/2)
##    b = int(n/2)
##
##    for i in range(int(n/2)):
##        if isPrime(a) == True and isPrime(b) == True:   ## 둘 다 소수일경우
##            print(a, b)
##            break
##        else:
##            a = a-1
##            b = b+1
## 



###07
##x, y, w, h = map(int, input().split())
##nl = [x, w-x, h-y, y]
##print(min(nl))


#08
##from collections import Counter
##xl, yl =[], []
##for i in range(3):
##    x, y = map(int, input().split())
##    xl.append(x)
##    yl.append(y)
##
##cx = Counter(xl).most_common()[1][0]
##cy = Counter(yl).most_common()[1][0]
##print(cx, cy)


#09
##while True:
####    a, b, c = map(int, input().split())
##    nl = list(map(int, input().split()))
##    nl.sort()       # nl = nl.sort() 오류 사항 블로그에 적기
##    a, b, c = nl[0], nl[1], nl[2]
##    if a == 0 and b == 0 and c == 0:
##        break
##    if c**2 == a**2+b**2:    ## 피타고라스 정리 해당
##        print('right')
##    else:
##        print('wrong')


#10
#인터넷
##import math
##r = int(input())
##print("{0:.6f}".format(r*r*math.pi))  ## 유클리드 기하학
##print("{0:.6f}".format(2*(r**2)))     ## 택시 기하학 


#11
import math

t = int(input())

for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = math.sqrt((x2-x1)**2+(y2-y1)**2)
    if d == 0 and r1 == r2:
        print(-1)
    elif abs(r1-r2) == d or r1+r2 == d:
        print(1)
    elif abs(r1-r2) < d < (r1+r2):
        print(2)
    else:
        print(0)
    


    
