#01
##a, b, c = map(int, input().split())
####for i in range(20):
####    if a+(b*i) < c*i:
####        print(i)
####        break
####    else:
####        print('-1')
####        break
### 인터넷 참고
##if b >= c:  # 가변비용이 노트북 가격보다 같거나 크
##    print(-1)
##else:
##    print((int)(a/(c-b))+1)  ## 딱 같아지는 시점(=아직 이익 발생 전): a/(c-b),
##                        ## 이익이 발생하려면 그 전 시점보다 +1해야된다.


###02
##n = int(input())
##cnt=1    ## 방의 개수
##while n > 1:  #입력이 1인 경우는 실행x
##    n -= (6*cnt)    ##입력받은 수에서 6*cnt씩 빼기
##    cnt+= 1         # 그 후 cnt 증가
##print(cnt)  


#03
##n = int(input())
##line ## 대각선
##dcnt = 1
##while True:
n = int(input())
line = 1  ## 몇 번째 대각선?

while n > line:         ## 어느 그룹에 들어갈 것인가?(어느 행)
    n-=line
    line += 1
    
if line%2==0:  ## 짝수 일때
    a=n        ## 분자 그대로
    b=line-n+1 ## 분모 내림차순
    
else:
    a=line-n+1
    b=n

pirnt(a,'/',b,sep="")
    
    

#04
##a, b, v = map(int, input().split())
####day = 0
####v1 = 0
####
####while v1 < v:       ## v1값이 v값이라 같아지면 같은 높이에 오름
####    v1 += (a-b)
####    day += 1    ## day값 증가시켜 며칠 걸리는지 알아보기    
####print(day)       #----------시간 초과
####d = 1
####while True:
####    if (v == (a-b)*d):
####        print(d)
####        break
####    else:
####        d += 1
###-----
##d = (v-b)/(a-b)   
##if d == int(d):
##    print(int(d))
##else:
##    print(int(d)+1)         ##2.3일 이렇게 나오면 3일로 계산하기 위해서
        
            
#05
##내가 직접
##T = int(input())
##for i in range(T):
##    h, w, n = map(int, input().split())
##    
##    if n%h != 0:   ##            
##        y = n%h   ## 층수
##        x = int(n/h) + 1  # 현재 몫+1이 다음  호수
##    else:
##        y = h   ## 높이가 층수
##        x = n/h     ## 어차피 호수
##    if x < 10:
##        floor = str(y)+'0'+str(x)
##        print(int(floor))
##    else:
##        floor = str(y)+str(x)
##        print(int(floor))
#### 인터넷 참고
##T = int(input())
##
##for i in range(T):
##    h, w, n = map(int, input().split())
##    y = n % h     #층수
##    x = n//h+1    ## 호수(몫+1)
##
##    if n % h == 0:   ## 나누어 떨어질때
##        y = h       ## 호텔 높이가 층수
##        x -= 1      ## 나눈 몫, 즉 위에서 계산한 x에서 -1하기
##    print(y*100+x)   ## 굳이 str로 형변환 할 필요x
    


#06
##t = int(input())
####sum = 0
####for i in range(t):
####    k, n = map(int,input().split())
####    if n == 1:   ## 1호에 살면
####        print(1)
####    else:
####        for i in range(1, n+1):
####            sum += i
####        print(sum)
##for i in range(t):
##    k = int(input())
##    n = int(input())
##    sum = [i for i in range(1, n+1)]    ## 호수를 리스트화, 3호면 [1, 2, 3]
##
##    for _ in range(k):  ## k층을 제외한 층
##        for j in range(1, n):
##            sum[j] += sum[j-1]
##    print(sum[n-1])
##            


#07
##n = int(input())
##count = 0 ## 총 설탕봉지
##while n >= 0:
##    if n% 5 ==0:   # 설탕이 5의 배수만큼 있을때
##        count += n//5   # 몫이 총 봉지수
##        print(count)
##        break
##    n -= 3   ## 그렇지 않으면, 설탕이 5의 배수가 될때까지 반복
##    count += 1  ## 이때 증가하는 것은 3kg 설탕 봉지수
##else:
##    print(-1)  ## 못구하면 -1


#08
##a, b = map(int, input().split())
##s = [a,b]
##print(sum(s))    ## sum함수 짚고 넘어가기
##----더 쉬운거
#print(a+b)

