import sys

n=int(sys.stdin.readline().rstrip())
n_list= list(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline().rstrip())
m_list = list(map(int,sys.stdin.readline().split()))
dict={}
for i in n_list:
    if i in dict:
        dict[i] +=1
    else:
        dict[i] = 1
n_set = set(n_list)
for i in m_list:
    if i in n_set:
        print(dict[i], end=' ')
    else:
        print(0, end=' ')