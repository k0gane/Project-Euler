m = 600851475143
n = int(pow(m, 0.5))
ans = 1
for i in range(2, n):
    if(m % i == 0):
        ans = i
        while m % i == 0:
            m = m / i
    if(m == 1):
        break
print(ans)