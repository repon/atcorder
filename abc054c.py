import itertools

N, M = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(M)]
print(AB)
print((1, 2).index(AB))
# for route in itertools.permutations(range(N), N):
#     print(route)
#     for points in range(N - 1):
