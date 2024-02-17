from collections import defaultdict


def main():
    N = int(input())
    S = tuple(map(int, input().split()))
    T = tuple(map(int, input().split()))
    dict_t = defaultdict(list)
    dict_next = defaultdict(list)  # 次に宝石を渡す時刻と相手
    for i in range(N):
        dict_t[T[i]].append(i)
    sg = [0] * N  # 初めて宝石をもらった時刻
    mtime = 100 ** 9
    for t in range(mtime):
        # 高橋くんから宝石をもらえるか？
        if t in dict_t:
            for i in dict_t[t]:
                # 初めてならsgに記録
                if sg[i] == 0:
                    sg[i] = t
                # もらった宝石を相手に渡す時刻を記録
                dict_next[t + S[i]].append(i)

        # 誰かが次の人に宝石を渡すか？
        if t in dict_next:
            for i in dict_next[t]:
                next = i + 1
                if next >= N:
                    next = 0
                # 初めてもらったのか？
                if sg[next] == 0:
                    sg[next] = t
                # もらった宝石を相手に渡す時刻を記録
                dict_next[t + S[next]].append(next)
        # もしsgに0がなければ終わり
        if 0 in sg:
            continue
        else:
            break

    for i in sg:
        print(i)


main()
