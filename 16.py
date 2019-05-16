a = 2**1000
print(a)
sum = 0
while a!=0:
    b = a % 10
    print(b)
    sum += b
    print(sum)
    a = a // 10  
