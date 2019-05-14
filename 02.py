fib = []
fib.append(1)
fib.append(2)
sum = 2
for i in range(2, 34):
    fib.append(0)
    fib[i] = fib[i-2] + fib[i-1]
    if(fib[i] % 2 == 0):
        sum += fib[i]
print(sum)

