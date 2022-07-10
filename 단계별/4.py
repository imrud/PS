###1
##while True:
##    a, b = map(int, input().split())
##    if(a==0 and b == 0):
##        break;
##    else:
##        print(a+b)



###2
##while True:
##    try:
##        a,b = map(int, input().split())
##        print(a+b)
##    except:
##        break
    

#3
n = int(input())
count = 0
sn = n

while True:
    ten = sn//10   # 10의 자리
    one = sn%10    # 1의 자리
    sum = ten + one   # 합
    so = sum%10    ## 합의 일의 자리(가장 오른쪽 자리 수)
    sn = str(one)+str(so)
    count += 1     ## 사이클 수 계산
    sn = int(sn)
    if (sn == n):   ## n과 같아질때
        break;
print(count)
    
    
    




