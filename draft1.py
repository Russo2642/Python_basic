a = 1
b = 2
c = 3

if a>b and b<c and c>a:
    print("a bolshe vseh, c menshe vseh")
else:
    print("a menshe vseh, c bolshe vseh")

print(len("hello")) 

import sys

x = 2
sys.getsizeof(x)


print(type(1))
print(type("test"))
print(type(" "))


total_sum=0
i=0
while i<10:
    total_sum+=i
    i+=1
print(i)

d = range(1,5)
total_sum2=0

for elements in d:
    total_sum2+=elements
print(total_sum2)

f = ["hi", 'hello', 'hola']
for words in f:
    print(words)

import sys

print(sys.getsizeof('this'))