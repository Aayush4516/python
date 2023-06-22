x='John'
y=4
z=['Aayush','Kunal']

print(type(x),type(y),type(z))

#assigning multiple values
x, y, z = "Orange", "Banana", "Cherry"
print(x)

x=y=z=10
print(x)
print(y)
print(z)

temp=[23,45,67]
a,b,c=temp
print(a)
print(b)
print(c)

temp=[23,45,67,49]
a,b,*c=temp
print(a)
print(b)
print(c)

x=None
print(type(x))