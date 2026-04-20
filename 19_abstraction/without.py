# Without Abstraction

# Laptop Contract: Government said these are must features for building laptops

# Concrete Class 
class Laptop:
    
    # Concrete Methods: Normal methods with implementation 
    def processor(self):
        print("Laptop With Processor")
        
    def ram(self):
        print("Laptop With RAM")
        
    def hdd(self):
        print("Laptop With Hard Disk")
        
    def nw(self):
        print("Laptop With Wifi Module")
        
# Implementations: Companies who wants to manufacture laptops

class Dell(Laptop):
    
    def processor(self):
        print("Dell Laptop With Processor") 
        
    def ram(self):
        print("Dell Laptop With RAM")
        
        
class Lenovo(Laptop):
    
    def hdd(self):
        print("Lenovo Laptop With Hard Disk") 
        
    def nw(self):
        print("Lenovo Laptop With Wifi Module")
        
# End Users 
print("Customer Buying Dell Laptop")
dell = Dell()
dell.processor()
dell.ram()
print("Dell Was Able To Sell a non functional laptop")


print("Customer Buying Lenovo Laptop")
lenovo = Lenovo()
lenovo.hdd()
lenovo.nw()
print("Lenovo Was Able To Sell a non functional laptop")