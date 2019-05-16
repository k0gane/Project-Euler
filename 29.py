num = []
for i in range(2, 101):
    for j in range(2, 101):
        a = pow(i, j)
        if not (a in num):
            num.append(pow(i, j))
print(len(num))
