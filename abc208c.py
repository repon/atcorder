def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    ALL = K // N
    mod = K % N
    add_ai_limit = sorted(A)[mod - 1] if mod > 0 else 0
    for i in range(N):
        if A[i] <= add_ai_limit:
            print(ALL + 1)
        else:
            print(ALL)


main()
