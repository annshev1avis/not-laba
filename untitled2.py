#записываем старт, финиш в отдельный список лыжника1
time1=[]
for i in range(4):
    time1.append(int(input()))


#записываем старт, финиш в отдельный список лыжника2
time2=[]
for i in range(4):
    time2.append(int(input()))


t1=(time1[2]*60+time1[3])-(time1[0]*60+time1[1])
t2=(time2[2]*60+time2[3])-(time2[0]*60+time2[1])
print(t1, t2)
if t1<t2:
    print(1)
else:
    print(2)