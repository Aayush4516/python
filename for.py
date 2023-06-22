fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

print('\n')

for x in fruits:
   if x is'banana':
      break
   print(x)
   
for x in range(6):
  print(x)

print('\n')

for x in range(1,6):
  print(x)

print('\n')


for x in range(1,6,2):
 print(x)

#iterator
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

#pass
x=1
for x in range(6):
  pass