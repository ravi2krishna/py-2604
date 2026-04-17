# Inheritance Types 

class Father:
    def house(self):
        print("Has House")
        
class Son: # No Inheritance
    def car(self):
        print("Has Car")
        
son_obj = Son()
son_obj.car()
# son_obj.house() # AttributeError: 'Son' object has no attribute 'house'

print("=" * 50)

# Single Level Inheritance: One Parent -> One Child 
class Father:
    def house(self):
        print("Has House")
        
class Son(Father): 
    def car(self):
        print("Has Car")
        
son_obj = Son()
son_obj.car()
son_obj.house() 

print("=" * 50)

# Multi Level Inheritance: Grand Parent -> Parent -> Child   

class GrandFather:
    def land(self):
        print("Has Land")

class Father(GrandFather):
    def house(self):
        print("Has House")
        
class Son(Father): 
    def car(self):
        print("Has Car")
        
son_obj = Son()
son_obj.car()
son_obj.house() 
son_obj.land() 

print("=" * 50)

# Multiple  Inheritance: One Child -> Multiple Parents

class GrandFather:
    def land(self):
        print("Has Land")

class Father(GrandFather):
    def house(self):
        print("Has House")

class Mother:
    def gold(self):
        print("Has Gold")
        
class Son(Father,Mother): # Multiple  Inheritance 
    def car(self):
        print("Has Car")
        
son_obj = Son()
son_obj.car()
son_obj.house() 
son_obj.land() 
son_obj.gold() 

print("=" * 50)

# Hierarchial Inheritance: One Parent -> Multiple Child

class GrandFather:
    def land(self):
        print("Has Land")

class Father(GrandFather):
    def house(self):
        print("Has House")

class Mother:
    def gold(self):
        print("Has Gold")

class Daughter(Father):
    def business(self):
        print("Has Business")
        
class Son(Father): # Multiple  Inheritance 
    def car(self):
        print("Has Car")
        
son_obj = Son()
son_obj.car()
son_obj.house() 
son_obj.land() 

daughter_obj = Daughter()
daughter_obj.business()
daughter_obj.house()

print("=" * 50)

# Hybrid Inheritance: Combination Of Inheritance Types 
class A:
    def a(self):
        print("A")
        
class B(A):
    def b(self):
        print("B")

class C(A):
    def c(self):
        print("C")
        
class D(B,C):
    def d(self):
        print("D")
        
obj_d = D()
obj_d.a()
obj_d.b()
obj_d.c()
obj_d.d()