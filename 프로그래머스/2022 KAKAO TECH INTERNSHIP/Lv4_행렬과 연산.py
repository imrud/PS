def solution(rc, operations):
    matrix = rc
    for op in operations:
        if op == 'ShiftRow':
            matrix.insert(0, matrix.pop())
        #print(matrix)      ## ShiftRow 확인
        else:
            tmp1 = matrix[0][0]
            tmp2 = matrix[0][-1]
            tmp3 = matrix[-1][0]
            tmp4 = matrix[-1][-1]
            
            ##1. (첫 행-끝 열)고정 / 아래쪽 이동
            for i in range(len(matrix[0])-1, 0, -1):
                #tmp1 = matrix[0][i]  
                matrix[0][i] = matrix[0][i-1]
            matrix[0][0] = 0    ## 비워 놓기
            #print(matrix)     ## r1확인
            #print(tmp1)

            ## 2. (끝 열-끝 행)고정/아래쪽 이동
            
            for i in range(len(matrix)-1, 0, -1):
                matrix[i][-1] = matrix[i-1][-1]
##                if i == 0:      ## 마지막열-첫행에 tmp1 삽입
##                    matrix[i][-1] = tmp1
##                else:
##                    matrix[i][-1] = matrix[i-1][-1]
            matrix[1][-1] = tmp2
            #print(matrix)      ## r2 확인

            ## 3. (끝 행-첫 열)고정/왼쪽 이동
            for i in range(0, len(matrix[0])-2):
                matrix[-1][i] = matrix[1][i+1]
            matrix[-1][3] = tmp4
            print('a: ',matrix)       ## r3 확인

            ## 4. (첫 열-첫 행)고정/위 쪽 이동
            for i in range(1, len(matrix)):
                if i == len(matrix)-1:
                    matrix[i][0] = tmp1
                else:
                    matrix[i][0] = matrix[i+1][0]
            #matrix[0][0]
        
    return matrix
