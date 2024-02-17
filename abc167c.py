def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for _ in range(N):
        line = list(map(int, input().split()))
        C.append(line[0])
        A.append(line[1:])

    result = -1
    #  Nをbit全探索（参考書数はN冊）
    #  1 << N == 2 ** N
    for bit in range(1 << N):
        c = 0
        skill = [0] * M
        for i in range(N):
            if (bit >> i) & 1:  # 買った場合
                c += C[i]
                for j in range(M):
                    skill[j] += A[i][j]
                if min(skill) >= X:
                    if result == -1:
                        result = c
                    else:
                        result = min(result, c)
            # else # 買わなかった場合
    print(result)


main()
