###6
##num1, num2 = map(int, input().split())
##if num2 < 10:
##    print(num1-num2)

###7
##num1, num2 = map(int, input().split())
##if num2 < 10:
##    print(num1*num2)


###8
##num1, num2 = map(int, input().split())
##if num2 < 10:
##    print(num1/num2)


###9
##num1, num2 = map(int, input().split())
##if num1 > 1 and num2 < 10000:
##    print(num1+num2)
##    print(num1-num2)
##    print(num1*num2)
##    print(num1//num2)
##    print(num1%num2)


###10
##num1, num2, num3 = map(int, input().split())
##if 2 <= num1 and num2 and num3 <= 10000:
##     print((num1+num2)%num3)
##     print(((num1%num3) + (num2%num3))%num3)
##     print((num1*num2)%num3)
##     print(((num1%num3)*(num2%num3))%num3)
##

#11
num1 = int(input())
num2 = int(input())

print(num1 * (num2%10))    ## 1의 자리
print(num1 * ((num2%100)//10))  ## 10의 자리
print(num1 * (num2//100))    ## 100의 자리

print(num1*num2)
    
