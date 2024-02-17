import time

# 時間計測開始
time_sta = time.perf_counter()
# 処理を書く（ここでは5秒停止する）
T = 10 ** 1
for _ in range(T):
    # tmp = (1 << _) & 1
    # tmp = (2 ** _) & 1
    print(1 << _)
    print(2 ** _)

# 時間計測終了
time_end = time.perf_counter()
# 経過時間（秒）
tim = time_end - time_sta

print(tim)
