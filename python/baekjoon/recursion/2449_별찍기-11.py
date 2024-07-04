def transform(base):
    p = len(base)
    t=[]
    for i in base:
        t.append(' ' * p + i + ' ' * p)
    for i in base:
        t.append(i + ' ' + i)
    return t
base = ['  *  ', ' * * ', '*****']
n=int(input())
while len(base) != n:
    base = transform(base)
print(base)
for i in base:
    print(i)