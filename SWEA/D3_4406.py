## 4406.모음이 보이지 않는 사람
import sys
T = int(input())

for test_case in range(1, T + 1):
    word = input()
    vowel = ['a', 'e', 'i', 'o', 'u']

    res = ''
    for i in word:
        if i not in vowel:
            res += i

    print('#{} {}'.format(test_case, res))
            
        
    
