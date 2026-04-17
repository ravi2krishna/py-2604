class A:
    def __init__(self,a):
        self._a = a # protected
        
obj = A(10)

# print(obj.a)

class B(A):
    def showA(self):
        a = A(10)
        print(a._a)

obj = B(20)
obj.showA()

