cnt = 0
def change(n):
    one = [3, 3, 5, 4, 4, 3, 5, 5, 4]
    ten = [3, 6, 6, 5, 5, 5, 7, 6, 6]
    teen = [6, 6, 8, 8, 7, 7, 9, 8, 8]
    d = n // 100
    e = (n - d * 100) // 10
    f = n - d * 100 - e * 10
    if n >= 11 and n <= 19:
        return teen[n-11]
    elif d == 0:
        if e == 0:
            return one[f-1]
        elif f == 0:
            return ten[e-1]
        else:
            return ten[e-1] + one[f-1]
    elif e == 0:
        if f == 0:
            return one[d-1] + 7
        else:
            return one[d-1] + 10 + one[f-1]
    else:
        if f == 0:
            return one[d-1] + 10 + ten[e-1]
        elif e == 1:
            return one[d-1] + 10 + teen[f-1]
        else:
            return one[d-1] + 10 + ten[e-1] + one[f-1]

sum = 0
for i in range(1, 1000):
    sum += change(i)
sum += 11
print(sum)