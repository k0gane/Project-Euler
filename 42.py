path = 'C:\\Users/Taisuke Moriwaki/PE/q42.txt'

def alp2num(c):
    return ord(c) - 96 

num = []
m = 0
for i in range(1, 31):
    m += i
    num.append(m)
print(num)

f = open(path)
data = f.read()
data1 = [name.strip('"') for name in data.split(',')]
data1.sort()
sum = 0
cnt = 0
for i , name in enumerate(data1):
    name1 = name.lower()
    score = 0
    a = list(name1)
    for j in range(len(a)):
        score += alp2num(a[j])
    print(score)
    if (score in num): cnt += 1
print(cnt)
