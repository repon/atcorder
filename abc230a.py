n = int(input())

if n >= 42:
    n = n + 1

str_n = str(n).zfill(3)

print("AGC" + str_n)
