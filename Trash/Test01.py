print("World")
#les go



#List
List = [1, 2, 3]
del List[0]
print(List[0:2])

#Tuple
Tuple = ('a1', 'b2', 'c1')

#dictionary
dic1 = {'name':'Ethan', 'age':19, 'work':'dev'}
dic2 = {'name':'Sunyeop', 'age':28, 'work':'str'}
dic3 = {'name':'Chris', 'age':21, 'work':'dev'}
dic1['appearance'] = 'hot'

print(dic1['name'])
print(dic1)
print(dic1.keys())
print(dic1.values())
print(dic1.items())

for k in dic1.keys():
  print(k)

#get
#print(dic1['height'])
print(dic1.get('height', 'age'))
print('height' in dic1)

#group
s1 = set([1,2,3,3,3])
s2 = {3,4,5}

print(s1)
print(s2)

s3 = s1 & s2
s4 = s1 | s2
s5 = s1 - s2
print(s3)
print(s1.intersection(s2))
print(s4)
print(s1.union(s2))
print(s5)
print(s1.difference(s2))

s1.add(4)
print(s1)
s1.update([5,6,7])
print(s1)


#Boolean
from copy import copy
ListA = [1,2,3,4,5,6,7,8,9]
if ListA:
  ListA.pop()
  print(ListA)

ListB = ListA[:]
ListC = copy(ListA)

print(ListA)
print(ListB)
print(ListA is ListB)
print(ListC)

#plus
YG, HY, SY = ('hamsome', 'hot', 'cute')
print(YG, HY, SY)
YG, HY = HY, YG
print(YG, HY, SY)
JH, SJ = 'pretty', 'beautiful'
print(JH, SJ)


#if
if JH == 'pretty':
  print("Juhae is pretty!")

#repeat
result = [num*3 for num in s1 if num%2 == 0]
print(result)
result1 = list(set([x*y for x in range(1, 9) for y in range(1, 19)]))

print(result1)

#function
def sum(*args):
  sum = 0
  for i in args:
    sum = sum + i
  return sum, sum+1
print(sum(499, 1, 334, 566, 677)[1])

#input
number = input("숫자를 입력하세요: ")

#files
f = open("presidentList.txt", 'w', encoding="UTF-8")
PList = ['Park', 'Moon', 'Yoon', 'Lee']
for i in PList:
  f.write(i + '\n')
f.close