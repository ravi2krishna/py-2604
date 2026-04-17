# Private Access

class A:
    def __init__(self,a):
        self.__a = a # private
        
obj = A(10)

# print(obj.a) # NOT ACCESSIBLE -> AttributeError: 'A' object has no attribute 'a'

# Python = "You shouldn't, but if you insist you can"
print(obj._A__a)

# Real World Application Scenario 
# Credit Card -> Sensitive Information -> CardNumber & CardPin 
class CreditCard: # No Proper Encapsulation
    def __init__(self,card_number,card_pin):
        self.card_number = card_number # Regular way is public 
        self.card_pin = card_pin # Regular way is public 
        
hdfc_credit_card = CreditCard("930398333383093","1234")

print(hdfc_credit_card.card_number)
print(hdfc_credit_card.card_pin)

# Real World Application Scenario 
# Credit Card -> Sensitive Information -> CardNumber & CardPin 
class CreditCard: # Proper Encapsulation
    def __init__(self,card_number,card_pin):
        self.__card_number = card_number # Regular way is public 
        self.__card_pin = card_pin # Regular way is public 
        
hdfc_credit_card = CreditCard("930398333383093","1234")

print(hdfc_credit_card.card_number)
print(hdfc_credit_card.card_pin)