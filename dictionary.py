dict1={
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#accessing elements
print(dict1)

print(dict1["brand"])

print(dict1.get("brand"))


print(dict1.keys()) #prints keys

print(dict1.values()) #print values

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["color"] = "red"

print(x) #after the change

# check if key exists

if "model" in dict1:
  print("Yes, 'model' is one of the keys in the thisdict dictionary") 

#adding in dictionary
dict1.update({"color": "red"}) 
print(dict1.keys())

#remove elements from a dictionary
dict1.pop("color")
print(dict1)

#loop in dictionary
for x in dict1:
  print(x)

for x in dict1:
 print (dict1[x])

for x in dict1.items():
 print(x)

print("\n")
#copy of dictionary

dict2=dict1.copy()
print(dict2)
print("\n")

#nested dictionaries
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
} 

print(myfamily)

print(myfamily["child1"]["name"])