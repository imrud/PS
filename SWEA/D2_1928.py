T = int(input())
decode = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
          'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
          '0','1','2','3','4','5','6','7','8','9','+','/']

for test_case in range(1, T + 1):
    word = input()
    w_len = len(word)
    tmp =''     ## word를 이진수로 변환후 하나로 만들기
    res = ''    ## 정답

    for i in range(w_len):
        num = decode.index(word[i])
        bin_num = str(bin(num)[2:])     ## 이진수로 변환 후, 0b는 제외하기

        while len(bin_num) < 6:     ## 이진수 길이가 6보다 작으면 앞에 0붙여주기
            bin_num = '0' + bin_num

        tmp += bin_num

    # 글자의 길이 * 6에서 8비트씩 자름
    for i in range(0, len(tmp), 8):
        res += chr(int('0b' + tmp[i:i + 8], 2))


    print('#{} {}'.format(test_case, res))
