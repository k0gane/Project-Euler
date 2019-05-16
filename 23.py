def d(n):
    sum = 0
    for i in range(1, (n // 2)+1):
        if n % i == 0:
            sum += i
    return sum

ans = 2
for i in range(3, 28124):
    if i < d(i): ans += i
print(ans)