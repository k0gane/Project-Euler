sum1 = 0
sum2 = 0
for i in range(1, 101):
    sum1 += i * i
for i in range(1,101):
    sum2 += i
    sum2 = pow(sum2, 2)
print(sum2 - sum1)