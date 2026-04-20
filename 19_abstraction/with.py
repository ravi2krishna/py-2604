# With Abstraction 

# Laptop Contract: Government said these are must features for building laptops

# Abstract Class 
from abc import ABC, abstractmethod 

class Laptop(ABC):
    
    # Abstract Methods: Methods without implementation 
    @abstractmethod
    def processor(self):
        pass 
    
    @abstractmethod
    def ram(self):
        pass 
    
    @abstractmethod
    def hdd(self):
        pass 
    
    @abstractmethod
    def nw(self):
        pass 
    
# Implementations: Companies who wants to manufacture laptops

class Dell(Laptop):
    
    def processor(self):
        print("Dell Laptop With Processor") 
        
    def ram(self):
        print("Dell Laptop With RAM")
        
    def hdd(self):
        print("Dell Laptop With Hard Disk")
        
    def nw(self):
        print("Dell Laptop With Wifi Module")
        
class Lenovo(Laptop):
    
    def processor(self):
        print("Lenovo Laptop With Processor") 
        
    def ram(self):
        print("Lenovo Laptop With RAM")
    
    def hdd(self):
        print("Lenovo Laptop With Hard Disk") 
        
    def nw(self):
        print("Lenovo Laptop With Wifi Module")
        
# End Users 
print("Customer Buying Dell Laptop")
dell = Dell() # TypeError: Can't instantiate abstract class Dell without an implementation for abstract methods 'hdd', 'nw'
dell.processor()
dell.ram()
dell.hdd()
dell.nw()
print("Dell Was Able To Sell a functional laptop")

print("Customer Buying Lenovo Laptop")
lenovo = Lenovo() # TypeError: Can't instantiate abstract class Lenovo without an implementation for abstract methods 'processor', 'ram'
lenovo.processor()
lenovo.ram()
lenovo.hdd()
lenovo.nw()
print("Lenovo Was Able To Sell a functional laptop")