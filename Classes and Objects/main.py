# class car:
#     x=5
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
        
#     def f1(self):
#         print(f"{self.a}")

#     @classmethod
#     def f2(cls):
#         print(cls.x+2)

# car1=car(2,5)
# car2=car(6,7)
# print(car1.x)
# print(car1.a)
# print(car1.b)
# car1.f1()

# car.f2()

# class Employee:
#     def __init__(self,id,name,salary):
#         self.id=id
#         self.name=name
#         self.salary=salary

#     def display(self):
#         print(f"Employee Id: {self.id}\nEmployee Name: {self.name}\nEmployee Salary: {self.salary}")


# e1=Employee(244,"Taha",200000)
# e1.display()




# # Question 1
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
    
#     def show(self):
#         print(f"Nmae: {self.name}\nAge: {self.age}")

# p1=Person("taha",20)
# p1.show()

# Question 2
# class Circle:
#     def __init__(self,radius):
#         self.radius=radius

#     def setRadius(self,radius):
#         self.radius=radius

#     def getRadius(self):
#         print(self.radius)

#     def Area(self):
#         print("Area : ",(22/7)*(self.radius**2))

#     def Circumference(self):
#         print("Area : ",2*(22/7)*(self.radius))

# r1=Circle(3)
# print(r1.radius)
# r1.setRadius(2)
# print(r1.radius)
# r1.getRadius()
# r1.Area()
# r1.Circumference()


# Quetion 3
# class Rectangle:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width

#     def setDimensions(self):
#         self.Dimensions=f"Length: {self.length} , Width: {self.width}"
        
#     def getDimensions(self):
#         print(self.Dimensions)

#     def getArea(self):
#         print(f"Area of Rectangle : {self.length*self.width}")


# r1=Rectangle(23,44)
# r1.setDimensions()
# r1.getDimensions()
# r1.getArea()


# Question 4
# class Book:
#     def __init__(self,bookid,title,price):
#         self.bookid=bookid
#         self.title=title
#         self.price=price
    
#     def show(self):
#         print(f"Book Id : {self.bookid}\nTitle : {self.title}\nPrice : {self.price}")

# b1=Book(1,"Chemistry",2000)
# b1.show()

# Question 5
class Team:
    def __init__(self):
        self.members=[]

    def addMember(self,member):
        self.members.append(member)
    
    def getMember(self):
        print("Team Member")
        for idx,i in enumerate(self.members):
            print(idx,i)

t1=Team()
t1.addMember("Taha")
t1.addMember("Hanzala")
t1.addMember("Anis")

t1.getMember()


        





