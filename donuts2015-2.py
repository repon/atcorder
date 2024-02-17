def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = []
    C = []
    I = []
    for _ in range(M):
        line = list(map(int, input().split()))
        B.append(line[0])
        C.append(line[1])
        I.append(line[2:])
    max_ability = 0


main()
