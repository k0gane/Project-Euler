prime = []
cnt = 0
for i in range(2, 200000):
    for j in range(1, int(pow(i+1, 0.5)+1)):
        if i % j == 0:
            cnt += 1
            break
    if cnt == 0:
        prime.append(i)
print(prime[10000])