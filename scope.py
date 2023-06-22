#global scope
x=10
def myfunction():
    x=5      #local scope
    print(x)
myfunction()
print(x)
 
#using nonlocal scope

def myfunc1():
  x = "John"
  def myfunc2():
    x = "hello"
  myfunc2()
  return x

print(myfunc1()) 

#difference when use nonlocal as it gives variable scope of outer function
def myfunc1():
  x = "John"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1()) 

#using global keyword to make local variable global
def myfunction():
  global x
  x = "Global"

myfunction()

#x should now be global, and accessible in the global scope.
print(x)
