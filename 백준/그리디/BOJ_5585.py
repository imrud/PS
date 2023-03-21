import sys

input = sys.stdin.readline

price = int(input())    ## 물건 가격(= 타로가 지불할 돈)
change = 1000-price

changes = [500, 100, 50, 10, 5, 1]   ## 잔돈
res = 0 ## 잔돈의 개수

for ch in changes:
    res += change // ch      ## 몫
    change = change % ch

print(res)



