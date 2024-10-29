import time
import random as rd

li = list(range(65260))
flg = 0

start = time.time()  # 現在時刻（処理開始前）を取得

# 実行したい処理を記述

end = time.time()  # 現在時刻（処理完了後）を取得

time_diff = end - start  # 処理完了後の時刻から処理開始前の時刻を減算する
print(time_diff)  # 処理にかかった時間データを使用

start = time.time()
rand = rd.randint(0,65259)

for i in li[rand:]:
    continue
if flg == 0:
    for i in li[:rand]:
        continue

end = time.time()

time_diff = end - start
print(time_diff)