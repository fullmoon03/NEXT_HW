
# number
print(1+1)
print (len("Hello World"))

import math
print(math.sqrt(4))
math.pow(4,2)

import random
random.random()

# string
'Hello world'
"Hello world"
'''
Hello
world
'''
'1'+'1'
len('Hello world'*1000)
'Hello world'.replace('world', 'universe')

#list
students = ["egoing", "sori", "maru"]
grades = [2,1,4]
students[1]
len(students)
min(grades)
sum(grades)

import statistics
statistics.mean(grades)
import random
random.choice(students)

#variables
name='sori'
message='hi, '+name+'.... bye, '+name+'.'
print(message)

#debug
a=1
b=2
c=3
d=4
a=2
e=5

#input&output
name=input('name:')

#pypi
# python standard library -> import로 불러옴
import pandas
house = pandas.read_csv('house.csv')
print(house)
print(house.head(2))
print(house.describe()) #mean, std, min, max 등등 데이터과학
#pandas 뿐만 아니라 pypi에서 검색해서 다 쓸 수 있음

#제어문(if 등), 함수 등등 공부하기!!