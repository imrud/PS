#01
##def factorial(n):
##    if n == 0 or n == 1:
##        return 1
##    else:
##        return n*factorial(n-1)
##
##n = int(input())
##print(factorial(n))


#02
##def fibonacci(n):
##    if n == 0:
##        return 0
##    elif n == 1:
##        return 1
##    else:
##        return fibonacci(n-1)+fibonacci(n-2)
##
##n = int(input())
##print(fibonacci(n))


#03
## 인터
##def print_star(n):
##    m = []
##    for i in range(3*len(n)):
##        if i//len(n) == 1:
##            m.append(n[i%len(n)] + " "*len(n)+n[i%len(n)])
##        else:
##            m.append(n[i%len(n)]*3)
##    return m
##
##n = int(input())
##star = ["***", "* *", "***"]
##
##e = 0   # 지수
##while n > 3:
##    n = n/3
##    e +=1   ##  입력받은 수가 3의 몇 승인지 계산
##
##for i in range(e):
##    star = print_star(star)
##for i in star:
##    print(i)




#04
##def hanoi(nl):
##    k = 0    # 옮긴 횟수
##    
##    return print(nl)
##        
##n = int(input())
##nl = []
##for i in range(n):
##    nl.append(i+1)
##hanoi(nl)
## 인터넷
##def hanoi(n, a, b, c):
##    if n == 1:
##        print(a, c)
##    else:
##        hanoi(n-1, a, c, b)
##        print(a, c)
##        hanoi(n-1, b, a, c)
##
##n = int(input())
##print(2**n - 1)
##hanoi(n, 1, 2, 3)

