x=5
y = 'John'
print(x,y)
print(type(x))

a,b,c = "Orange","Banana","Cherry"
print(a,b,c)
fruits = ["apple","strawberry","Plum"]
d,e,f = fruits
print (d,e,f)

xy = "awesome"
def myfunc():
    print("Python is:" +xy)
myfunc()

greet = "Hello World!"
print(greet[5:-2])
age = 37
txt="My name is john and i am {} years old"
print(txt.format(age))

a=33
b=33
if b>a:
    print("b is greater than a")
elif a ==b:
    print("a and b are equal")
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.keys()
print(x)  # before the change
car["color"] = "white"
print(x)  # after the change