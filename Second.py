import math
print(f'Hello, Yerevan')
def get_score(name,score):
    print(f"{name}'s age is {score / 10:5f}")
    print(f"goodbye")
    get_score('shkolnik',25)

T = (2,2,3)
T = (1,) + T[1:]
print(T)

for i in range(5):
    if i % 2 == 0:
        continue


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    print(factorial(5))
    print(5)
print(math.factorial(5))

x = [3,4]
def f(x):
    x[0]= 1
    x = [3,4]
f(x)
y = x
y.append(5)
y = 6
print(x)

a, *b, c = [1,2]
print(a,b,c)

# def sum(*args):
#     res=0
#     for x in args:
#         res +=x
#     return res
# sum(*{"A", "G", "C", "T"})

def f(x, l=[]):
    l.append(x)
    return l
print(f(1))

print(f(1))

def f(a, *args, **kwargs):
    print(a, args, kwargs)
f(1,2,3,x=4,y=5)

students = [
    {'name':'Dmitry','age': 18},
    {'neame': 'John', 'age': 23},
    {'name':'Lucy','age': 15},
]

print(students)
print(students)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)
print(p1.name)
print(p1.age)
print(p1)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

counter = 0
def f():
    counter += 1
f()
print(counter)