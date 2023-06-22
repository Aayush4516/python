s1={"apple","banana","pear"}
print(s1)
s2={1,2,3}
print(s2)

#length of set
print(len(s1))

for x in s1:
    print(x)

#adding elements to a set
s1.add("kiwi")
print(s1)

#adding list to a set
mylist = ["kiwi", "orange"]
s1.update(mylist)
print(s1)

#removing from set
s1.remove("kiwi")
print(s1)

s1.pop()
print(s1)

#looping in set

for x in s1:
    print(x)

#union intersection and symmetric difference

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)
print(z)

u=x.union(y)
print(u)

v=x.symmetric_difference(y)
print(v)

