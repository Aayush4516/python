a='hello'
print(a)

b='Aayush likes fight club'
print(b)

#string numbering
print(b[2])

print(b[0])

print(b[-1])
 
#length of string
print(len(a))

print("likes" in b)

#slicing in strings

print(b[2:5])

print(b[2:])

print(b[-4:-2])

#modify strings

print(b.lower())

print(b.upper())

print(b.strip())

print(b.replace('h','k'))

print(a.split('l'))

#concatenate strings

c=a+" " +b
print(c)

#format strings

age = 36
txt = "My name is Aayush, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} rupees for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

#escape sequence

print("hello \nAayush")

print("hello \'Aayush\'")
