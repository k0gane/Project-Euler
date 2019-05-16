num = 0
cnt = 0
max = 1
for i in range(2,1000000):
    m = i
    while m > 1:
        if(m % 2 == 0):
            m = int(m / 2)
        else:
            m = 3 * m + 1
        cnt += 1
    if num < cnt:
        num = cnt
        max = i
    cnt = 0
print(max)