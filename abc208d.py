import itertools

N, M = map(int, input().split())
abc = [list(map(int, input().split())) for _ in range(M)]
for p in itertools.permutations(range(1, N + 1), N):
    print(p)
