def recursion(n):
    if n == 1:
        return ['*']
    
    stars = recursion(n//3)
    a=[]
    
    for i in stars:
        a.append(i * 3)
    for i in stars:
        a.append(i + ' '*(n//3) + i)
    for i in stars:
        a.append(i * 3)
    return a

n=int(input())
print('\n'.join(recursion(n)))