T = int(input())

# 90도 회전하는 함수
def rotation(a, N):
    new_arr = [[0] * N for _ in range(N)]  # NxN 빈 배열 먼저 만들기// 90도 돌리고 반환 할 배열
    for i in range(N):
        for j in range(N):
            new_arr[i][j] = a[N-1-j][i]
    return new_arr

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    rot_90 = rotation(arr, N)
    rot_180 = rotation(rot_90, N)       ## 90도 돌린 배열 -> 90도 돌리면 180도
    rot_270 = rotation(rot_180, N)      ## 180도 돌린 배열 -> 90도 돌리면 270도

    print("#{}".format(tc))
    for i in range(N):
        print("".join(map(str, rot_90[i])), end=" ")
        print("".join(map(str, rot_180[i])), end=" ")
        print("".join(map(str, rot_270[i])), end=" ")
        print()
