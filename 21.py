def d(n):
    sum = 0
    for i in range(1, (n // 2)+1):
        if n % i == 0:
            sum += i
    return sum


print(d(6232))
ans = 0
for i in range(200, 10000):
    a = d(i)
    if d(a) == i and a != i:
        ans += i
print(ans)