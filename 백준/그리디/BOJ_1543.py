import sys

input = sys.stdin.readline
sentence = input().rstrip()
word = input().rstrip()
w_len = len(word)   ## 검색하고 싶은 단어의 길이

cnt = 0
cur = -1    ## 마지막 슬라이싱 위치
for i in range(len(sentence)):
    if i > cur:    ## 현재 위치와 마지막 위치가 같지 않을 경우
        if sentence[i:i+w_len] == word:     ## 문서 내 단어가 있다면
            cnt += 1
            cur = (i+w_len) - 1     ## 마지막 위치
            #print('cur : ' ,cur)

print(cnt)

## 다른 풀이 1
print(sentence.count(word))

## 다른 풀이 2
cnt = 0
cur = 0     ## 인덱스 길이
while cur <= len(sentence) - w_len:
    if sentence[cur : cur + w_len] == word:
        cnt += 1
        cur += w_len    ## 단어의 길이만큼 인덱스 증가
    else:       ## 찾지 못할 경우
        cur += 1        ## 인덱스 1 증가
print(cnt)
