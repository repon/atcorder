X = int(input())
if X >= 0:
    result = X // 10
else:
    # Xが負の場合の処理。Xが-10の倍数であればそのまま除算、そうでなければ1を引く
    if X % 10 == 0:
        result = X // 10
    else:
        result = X // 10 - 1
print(result)
