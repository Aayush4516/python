#lists are mutable and allows duplicates

l = ["apple", "banana", "cherry", "apple", "cherry"]
print(l)

l[1]='kiwi'
print(l)

#print length of list
print(len(l))

#print type of l
print(type(l))

#indexing
print(l[1])

print(l[-1])

print(l[2:])

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#changing list

temp = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
temp[1:3] = ["blackcurrant", "watermelon","pear"]
print(temp)

temp.insert(2,"cool")
print(temp)

#add items

temp.append('pomogrenate')
print(temp)

temp.extend(thislist)
print(temp)

#removing from list
temp.remove('apple')
print(temp)

temp.pop(2)
print(temp)

del temp[4]
print(temp)

#list comprehension

newlist=[x for x in temp if "a" in x]
print(newlist)

newlist=[x for x in temp if  x!='apple']
print(newlist)

newlist=[x for x in range(20)]
print(newlist)

newlist=[x.upper() for x in temp if "a" in x]
print(newlist)

#sort list
temp.sort()
print(temp)

temp.sort(reverse =True)
print(temp)

temp.sort(key=str.lower)
print(temp)

k=temp.copy()
print(k)

#looping in list
for x in temp:
 print(x)



