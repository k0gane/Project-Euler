def num(n):
    if n == 1: return 1
    else: return n * num(n-1)

a = num(100)
ans = 0
while a != 0:
    b = a % 10
    ans += b
    a = a // 10
print(ans)
