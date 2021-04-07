import csv

l = list(range(1000))
with open('data/realestatedata.csv','r',encoding='utf-8-sig') as f:
    for row in csv.reader(f):
        l.append(row)

for i in l:
    print(i)

detachedList=list(filter(lambda item:item[0]=='Detached',l))
print(detachedList)
