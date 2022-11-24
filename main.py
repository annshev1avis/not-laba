lst=[]
S=[]
m=int(input()) #строки
n=int(input()) #столбцы
for i in range(m):
    s=[]
    for x in input().split():
        y=int(x)
        s.append(y)
    lst.append(s)
for i in range(len(lst)):
    print(lst[i])
for i in range(m):
    s1=sum(lst[i])
    S.append(s1)
print(S)