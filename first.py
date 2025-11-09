# print("""Twinkle twinkle little star.
# How I wonder what you are.
# Up above the world so high.
# Like a diamond in the sky.
# Twinkle twinkle little star.
# How I wonder what you are.

# Twinkle twinkle little star.
# How I wonder what you are.
# Up above the world so high.
# Like a diamond in the sky.
# Twinkle twinkle little star.
# How I wonder what you are.""")

# class
# class Employee:
#     name = "harry"      here name is class attribute
#     lang = "py"
#     salary = 1200000
# abhi = Employee()
# abhi.age = 20    here age is instance(object) attribute
# abhi.name = "mohan"  note instance attribute take prefrence over class attribute
# print(abhi.name,abhi.salary,abhi.age,abhi.name)


# class Employee:
#     name = "harry"      
#     lang = "py"
#     salary = 1200000
#     def __init__(self):  #dunder method which is called automatically that is __ not all dunder method is called automically only __init__ this one
#         print("i am creating object")
#     def __init__(self,name,lang,salary):
#         self.name = name
#         self.lang = lang
#         self.salary = salary
#     def Getinf(self):
#         print(f"the name is {self.name} and salary is {self.salary}")
#     @staticmethod
#     def Greet():
#         print("good morning")
# abhi = Employee("harry","python",120000)
# # abhi.age = 20    
# abhi.name = "mohan"  
# print(abhi.name,abhi.salary,abhi.lang)
# abhi.Getinf()
# abhi.Greet() 
# # rohan = Employee()

# programmers working in microsoft
# class Programmer:
#     company = "microsoft"
#     def __init__(self,name,lang,salary):
#         self.name = name
#         self.lang = lang
#         self.salary = salary
# P = Programmer("harry","python",122000)
# print(P.name,P.salary,P.lang,P.company)

# sq,cue,root
# import math
# class Calculator:
#     def __init__(self,n):
#         self.n = n
#     def square(self):  
#         print(f"the square is {self.n*self.n}")  
#     def cube(self):  
#         print(f"the cube is {self.n*self.n*self.n}")  
#     def squareroot(self):  
#         print(f"the squareroot is {math.sqrt(self.n)}")  
#     def squareroot(self):  
#         print(f"the squareroot is {self.n**1/2}") 
#     @staticmethod
#     def Greet():
#         print("hello there")

# C = Calculator(4)
# C.Greet()
# C.square()
# C.cube()
# C.squareroot()
# C.squareroot()

# interesting

# class N:
#     a = 4

# p = N()
# print(p.a)
# p.a = 0
# print(p.a)
# print(N.a)#class attribute will not change

# train
# from random import randint
# class Train:
#     def __init__(self,trn):
#         self.trn = trn
#     def book(self,fro,to):
#         print(f"the train no {self.trn} from {fro} to {to} is running on time")
#     def fair(self,fro,to):
#         print(f"the train no {self.trn} from {fro} to {to} price is {randint(222,1234)}")
# t = Train(6501)
# t.book("bandra","mumbai")
# t.fair("bandra","mumbai")

# INHERITANCE that is multiple inheritance
# class Employee:
#     company = "itc"
#     def show(self):
#         print(f"the company name is {self.company} amd we r working there")
# class Coder:
#     language = "python"
#     def lang(self):
#         print(f"in the company u require {self.language} language is mandatory")      
# class Programmer(Employee, Coder):
#     salary = 12000
#     def cootie(self):
#         print(f"the company name is {self.company} and the language u required is {self.language} and the salary of the employee is {self.salary}")

# a = Employee()
# b = Programmer()
# b.show()
# b.lang()
# b.cootie()

# multilevel inheritance
# class Employee:
#     a = 1
# class Coder(Employee):
#     b = 2
# class Programmer(Coder):
#     c = 3

# o = Employee()
# print(o.a)
# o = Coder()
# print(o.a,o.b)
# o = Programmer()
# print(o.a,o.b,o.c)

# using super in this 

# class Employee:
#     def __init__(self):
#         print("hi")
#     a = 1
# class Coder(Employee):
#     def __init__(self):
#         print("hello")
#     b = 2
# class Programmer(Coder):
#     def __init__(self):
#         super().__init__()
#         print("its me")
#     c = 3


# o = Programmer()
# print(o.a,o.b,o.c)

# class methods

# class Employee():
#     a = 1
#     @classmethod
#     def show(cls):
#         print(f"the value of a is {cls.a}")

# e = Employee()
# e.a = 45
# e.show()

# using add because we cannot direct use + 
# class Number:
#     def __init__(self,n):
#         self.n = n
#     def __add__(self,num):
#         return self.n + num.n

# n = Number(1)
# m = Number(2)
# print(n + m)


# class Employee:
#     a = 1

#     @classmethod
#     def show(cls):
#         print(f"the attribute of class a is {cls.a}")
#     @property
#     def name(self):
#         return f"{self.fname} {self.lname}"
#     @name.setter
#     def name (self,value):
#         self.fname = value.split(" ")[0]
#         self.lname = value.split(" ")[1]

# e = Employee()
# e.a = 45
# e.name = "harry khan"
# print(e.fname,e.lname)
# e.show()

# class Twodvector:
#     def __init__(self,i,j):
#         self.i = i
#         self.j = j
#     def show(self):
#         print(f"the vector is {self.i}i + {self.j}j")

# class Threedvector(Twodvector):
#     def __init__(self,i,j,k):
#         super().__init__(i,j)
#         self.k = k

#     def show(self):
#          print(f"the vector is {self.i}i + {self.j}j + {self.k}k")
    
# a = Twodvector(1,2)
# a.show()
# b = Threedvector(1,2,3)
# b.show()    

# class Animals:
#     pass
# class Pets(Animals):
#     pass

# class Dog(Pets):
#     @staticmethod
#     def bark():
#         print("wow wow !")

# d = Dog()
# d.bark() 

# class Employee:
#     salary = 234
#     increment = 20

#     @property
#     def salaryAfterIncrement(self):
#         return (self.salary + self.salary * (self.increment/100))
    
#     @salaryAfterIncrement.setter
#     def salaryAfterIncrement(self,salary):
#         self.increment = ((salary/self.salary) - 1)*100

# e = Employee()
# print(e.salaryAfterIncrement)
# e.salaryAfterIncrement = 270
# print(e.increment)

# class Complex:
#     def __init__(self,r,i):
#         self.r = r
#         self.i = i
    
#     def __add__(self,c2):
#         return Complex(self.r + c2.r, self.i + c2.i)
#     def __str__(self):
#         return f" {self.r} + {self.i} i  "
    
# c1 = Complex(1,2)
# c2 = Complex(3,4)
# print(c1 + c2)

# class Complex:
#     def __init__(self, r, i):
#         self.r = r
#         self.i = i
    
#     def __add__(self, c2):
#         # (a + bi) + (c + di) = (a + c) + (b + d)i
#         return Complex(self.r + c2.r, self.i + c2.i)
    
#     def __mul__(self, c2):
#         # (a + bi)(c + di) = (ac - bd) + (ad + bc)i
#         real = self.r * c2.r - self.i * c2.i
#         imag = self.r * c2.i + self.i * c2.r
#         return Complex(real, imag)
    
#     def __str__(self):       temp.__str__()
#         # Display like "a + bi"
#         return f"{self.r} + {self.i}i"

# # Example
# c1 = Complex(1, 2)
# c2 = Complex(3, 4)

# print("Addition:", c1 + c2)             c1.__add__(c2)
# print("Multiplication:", c1 * c2)

# class Vector:
#     def __init__(self,x,y,z):
#         self.x = x
#         self.y = y
#         self.z = z
#     def __add__(self,other):
#         result = Vector(self.x + other.x , self.y + other.y , self.z + other.z)
#         return result
#     def __mul__(self,other):
#         result = self.x * other.x + self.y * other.y + self.z * other.z
#         return result
#     def __str__(self):
#         return f"Vector{self.x}i + {self.y}j + {self.z}k"
    

# v1 = Vector(1,2,3)
# v2 = Vector(1,2,3)
# v3 = Vector(1,2,3)
# print(v1+v2)
# print(v1*v2)

# class Vector:
#     def __init__(self,l):
#         self.l = l
    
#     def __len__(self):
#         return len(self.l)

# v1 = Vector([1,2,3])
# print(len(v1))

# import random
# n = random.randint(1,10)
# a = -1
# guess = 0
# while(a!=n):
#     guess += 1
#     a = int(input("guess the number : "))
#     if(a>n):
#         print("lower number please")
#     else:
#         print("higher number please")
# print(f"u have entered the right number {a} in {guess} attempts")

# if(n := len([1,2,3,4,5]))>3:
#     print(f"list is too long {n} elements expected < 3")

# def http_status(status):
#     match status:
#         case 200:
#             return "ok"
#         case 404:
#             return "not found"
#         case _:
#             return "unknown status"
        
# print(http_status(404))


# dict1 = {'a': 1, 'b':2}
# dict2 = {'c' :3, 'd':4}
# merged = dict1 | dict2
# print(merged)

# with open('file1.txt', 'w') as f1:
#     f1.write("hi")

# with open('file2.txt', 'w') as f2:
#     f2.write("cybersecurity expert.")
# with (
#     open('file1.txt') as f1,
#     open('file2.txt') as f2
# ):
#     data1 = f1.read()
#     data2 = f2.read()
#     print("File1 contents:", data1)
#     print("File2 contents:", data2)

# try:
#     a = int(input("enter a number : "))
#     print(a)
# except ValueError as v:
#     print(v)
# except Exception as e:
#     print(e)
# finally:
#     print("hey i am inside of finally")

# print("thank you")
# def main():
#     try:
#         a = int(input("enter a number : "))
#         print(a)
#         return
#     except ValueError as v:
#         print(v)
#         return
#     except Exception as e:
#         print(e)
#         return
#     finally:
#         print("hey i am inside of finally")
# print("thank you")

# # call the function
# main()



# a = int(input("enter a first number "))
# b = int(input("enter a  second number "))
# if(b==0):
#     raise ZeroDivisionError("hey in our program divison by zero is not possible")
# else:
#     print(f"the division is {a/b}")
# def myFunc():
#     print("hello world")

# if __name__ == "__main__":
#     print("we r directly runing this code")
#     myFunc()
#     print(__name__)

# a = 989
# def Func():
#     global a
#     a = 3
#     print(a)

# Func()
# print(a)
# index = 0
# l = [3,33,44]
# for i in l:
#     print(f"the item at {index} is {i}")
#     index +=1

# l = [3,2,3,4]
# for index, item in enumerate(l):
#     print(f"the item at {index} is {item}")

# myList = [3,76,56]
# squareLis = []
# for i in myList:
#     squareLis.append(i*i)


# print(squareLis)

# myList = [2,1,3,4]
# squareList = [i*i for i in myList]
# print(f"the square is {squareList}")
    
# try:
#     with open("1.txt","r") as f:
#         print(f.read())
# except Exception as e:
#     print(e)
# try:
#     with open("2.txt","r") as f:
#         print(f.read())
# except Exception as e:
#     print(e)
# try:
#     with open("3.txt","r") as f:
#         print(f.read())
# except Exception as e:
#     print(e)

# print("thank you!")

# l = [1,2,3,4,5,6,7]
# for i, item in enumerate(l):
#     if i == 2 or i == 4 or i == 6:
#         print(item)

# n = int(input("enter a number : "))
# table = [n*i for i in range(1,11)]
# print(table)


# try:
#     a = int(input("enter a number : "))    
#     b = int(input("enter a number : "))
#     print(a/b)
# except ZeroDivisionError as v:
#     print("infinite")

# n = int(input("enter a number : "))
# table = [n*i for i in range(1,11)]
# with open("table.txt","a") as f:
#     f.write("the table of" +n "is" +table )

# square = lambda x: x*x
# print(square(5))

# a = ["rohan","aman","akshay"]
# final = "::".join(a)
# print(final)

# a = "{} is a good {}".format("harry","boy")
# print(a)    

# l = [1,2,3,4,5]
# square = lambda x: x*x
# sqlist = map(square,l)
# print(list(sqlist))

# from functools import reduce
# l = [1,2,3,4,5,6]
# def even(n):
#     if(n%2==0):
#         return True
#     return False
# onlyEven = filter(even,l)
# print(list(onlyEven))

# def sum(a,b):
#     return a+b
# mul = lambda x,y:x*y
# print(reduce(sum,l))
# print(reduce(mul,l))

# name = input("enter name : ")
# marks = int(input("enter marks : "))
# number = int(input("enter number : "))
# s = "the name of student is {} his marks is {} and number is {}".format(name,marks,number)
# print(s)

# table = [str(7*i) for i in range(1,11)]
# s = "\n".join(table)
# print(s)
    
# def divisble5(n):
#     if(n%5==0):
#         return True
#     return False
# a = [5,10,45,63,24]
# f =list(filter(divisble5,a))
# print(f)

# from functools import reduce
# l = [5,10,45,63,24]
# def greater(a,b):
#  if(a>b):
#   return a
#  return b
# print(reduce(greater,l))


from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

app.run()

