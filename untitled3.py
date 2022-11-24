lst=[]
a=[]
m=int(input()) #строки
n=int(input()) #столбцы
i=0
while i<m:
    lst.append([])
    i+=1
print(lst)
i=0
j=0
while j<m:
    while i<n:
       lst[j].append(int(input()))
       i+=1
    i=0
    j+=1
print(lst)
