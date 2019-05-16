ans = 0
for i in range(2, 1000000):
    s = str(i)
    a = list(s)
    num = 0
    for j in range(len(a)):
        num += pow(int(a[j]), 5)
    if num == i: ans += num
print(ans)