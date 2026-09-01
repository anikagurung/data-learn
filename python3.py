list = [10,20,30,20,32,46]
d ={}
for x in list:
    if x in d:
        d[x] += 1
    else:
        d[x] = 1
print (d)
max_num = list[0]
for x in list:
    if x > max_num:
        max_num = x
print (max_num)
min_num = list[0]
for x in list:
    if x < min_num:
        min_num = x
print (min_num)
print ('***')

list = [10,20,30,30,20,30]
d ={}
for x in list:
    if x in d:
        d[x] += 1
    else:
        d[x] = 1
print (d)
max_count = 0
max_numm = 0
for x in d:
    value = d[x]
    if d[x] > max_count:
        max_count = d[x]
        max_numm = x
print(max_count)
print(max_numm)
print('&&&&')

line = "hello world hello nepal hello india"
words = line.split(' ')
print(words)
d = {}

for word in words:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1
print(d)


max_word = 0
max_letter = ""

for word in d:
    if d[word] > max_word:
        max_word = d[word]
        max_letter = word

print(max_word)
print(max_letter)
print('^^^^')
count = 0
vowel = ['a','e','i','o','u']
input = 'hello world'
for ch in input:
    if ch in vowel:
        count+=1
print (count)

list1 = ['a','b','c']
list2 = [1,2,3]
d={}

for i in range(len(list1)):
    value1 = list1[i]
    value2 = list2 [i]
    d[value1] = value2
print(d)