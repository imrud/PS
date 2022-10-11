## Facebook 인터뷰 : 문자열 재정렬
import sys
input = sys.stdin.readline

string = list(input().strip())

a = []
b = []
string.sort()
for s in string:
    if s.isalpha():
        a.append(s)
    else:
        b.append(s)


print("".join(a)+"".join(b))
        
