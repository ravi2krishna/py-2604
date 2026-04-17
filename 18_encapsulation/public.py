# Public Access

class A:
    def __init__(self,a):
        self.a = a # Regular way is public 
        
obj = A(10)

print(obj.a)