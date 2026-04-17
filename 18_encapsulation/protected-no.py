class A:
    def __init__(self,a):
        self.__a = a # private
        
obj = A(10)

# print(obj.a)

class B(A):
    def showA(self):
        a = A(10)
        print(a.__a)

obj = B(20)
obj.showA()

