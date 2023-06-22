#tuples
t1=("Aayush","Kartik","Kamal")
print(t1)

print(len(t1))

print(type(t1))

#indexing

print(t1[1])

print(t1[-1])

print(t1[0:2])

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple") 

#joinig tuples
thistuple+=t1
print(thistuple)

#unpacking tuples
(x,y,*z)=thistuple
print(x,y,z)

#looping
for x in thistuple:
  print(x) 

for x in range (len(thistuple)):
  print(thistuple[x]) 


