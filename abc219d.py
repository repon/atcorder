from itertools import combinations
import array

N = int(input())
X, Y = map(int, input().split())
bento = []
sum_bento = array.array("i", [0, 0])
for i in range(N):
    input_bento = list(map(int, input().split()))
    bento.append(input_bento)
    for j in range(2):
        sum_bento[j] += input_bento[j]
if sum_bento[0] < X or sum_bento[1] < Y:
    print(-1)
else:
    break_loop = False
    for i in range(2, N + 1):
        for comb_bento in combinations(bento, i):
            tmp_sum_bento = array.array("i", [0, 0])
            for tmp_bento in comb_bento:
                for j in range(2):
                    tmp_sum_bento[j] += tmp_bento[j]
            if tmp_sum_bento[0] >= X and tmp_sum_bento[1] >= Y:
                print(i)
                break_loop = True
                break
        if break_loop:
            break
