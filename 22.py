path = 'C:\\Users/Taisuke Moriwaki/PE/q22.txt'

def alp2num(c):
    return ord(c) - 96 
print(alp2num("a"))
print(alp2num("A"))

f = open(path)
data = f.read()
data1 = [name.strip('"') for name in data.split(',')]
data1.sort()
sum = 0
for i , name in enumerate(data1):
    name1 = name.lower()
    print(name1)
    score = 0
    a = list(name1)
    for j in range(len(a)):
        score += alp2num(a[j])
    sum += score * (i+1)
    print(score)
print(sum)

