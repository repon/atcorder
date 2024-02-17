a, b, c, d = 0, 0, 0, 0

for i in range(10):
    s = input()
    if "#" in s:
        if a == 0:
            c = s.find("#") + 1
            d = s.rfind("#") + 1
            a = i + 1
    else:
        if a > 0 and b == 0:
            b = i

if b == 0:
    b = 10

print(a, " ", b)
print(c, " ", d)
