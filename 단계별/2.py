###1
##a, b = map(int,input().split())
##
##if a > b:
##    print(">")
##elif a < b:
##    print("<")
##elif a == b
##    print("=")


###2
##score = int(input())
##
##if( 0 <= score <= 100):
##    if (90 <= score <= 100):
##        print("A")
##    elif (80 <= score <= 89):
##        print("B")
##    elif (70 <= score <= 79):
##        print("C")
##    elif (60 <= score <= 69):
##        print("D")
##    else:
##        print("F")
    

###3
##year = int(input())
##if (1 <= year <= 4000):
##    if((year%4==0) and (year%100 != 0 or year%400==0)):
##        print(1)
##    else:
##        print(0)


###4
##x = int(input())
##y = int(input())
##
##if x>0 and y>0:
##    print(1)
##elif x<0 and y>0:
##    print(2)
##elif x < 0 and y < 0:
##    print(3)
##else:
##    print(4)


###5
##h, m = map(int, input().split())
##
##if(h == 0):
##    if(m < 45):
##        h = 23      ## 시간 0으로 변함
##        m = 60+(m-45)
##    elif (m >= 45):
##        m = m-45
##
##else:
##    if(m < 45):
##        h = h-1
##        m = 60+(m-45)
##    elif (m >= 45):
##        m = m-45
##
##print(h, m)



