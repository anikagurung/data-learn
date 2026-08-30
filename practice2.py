data = [10,20,20,30,31,39]
print(data)
print (len(data))
for x in data:
    print(x)
print ('x')

for x in data:
    if x >= 30:
       print(x)
print('xx')

for x in data:
    if x%2==0:
        print('even number:',x)
for x in data:
    if x%2 == 1 and  x>35:
        print('odd number:', x )
for x in data:
    if x%2 == 1 or  x>35:
        print('odd number:', x )

data = [10,20,20,30,31,39]
count = 0
count1 = 0
for x in data:
    if x==20  :
        count += 1
    if x ==30:
        count1 += 1
print(count, count1)
print(20, count, 30, count1)

data = [10,20,20,30,31,39]
count2 =0
count3 = 0
occurence = []
for x in data:
    if x ==20:
        count2 = count2 +1
        occurence.append(count2)
print(count2, count3)
print(occurence)
print(20,count2,30,count3)

d={}
d[20]=1
print(d)
d[30] = 1
print(d)
d[20] = d[20]+1
print(d)
d[30] = d[30] +1
print(d)
print(20 in d)
print(50 in d)

data = [10,20,20,30,31,39]
d1 = {}
for x in data:
    if x in d1:
        d1[x] = d1[x] + 1
    else:
        d1[x]=1 #{10:1,20:2,30:1,31:1,39:1}
print(d1)
