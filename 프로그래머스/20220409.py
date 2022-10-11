def solution(array, commands):
    answer = []
    for c in commands:
        tmp = array
        for i, j, k in c:
            tmp = sorted(array[i:j])
            answer.append(temp[k])
    return answer
