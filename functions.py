#functions

def my_function():
  print("Hello from a function")

my_function()

def my_function(fname):
  print(fname + " Rothschild")

my_function("Emil")
my_function("Tobias")

#*args get arguments as tuple

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus") 

print('\n')

def my_function(child2, child1):
  print("The youngest child is " + child2)

my_function(child1 = "Aayush", child2 = "Tobi") 

#**kwargs to get aguments as dictionary
print('\n')

def my_function(**temp):
  print("The youngest child is " + temp["child1"])

my_function(child1 = "Aayush", child2 = "Tobi")

#default arguments

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("India")
my_function()

#returning answer

def temp(x):
 return x+5

print(temp(5))
