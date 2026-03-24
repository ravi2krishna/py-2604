# Tuple Methods / Operations On Tuples 

# index(): Used to get the index position of value 
data = (10,20,30,40,50)
print(data)
print(data.index(20))
# print(data.index(90)) # ValueError: 90 is not in list

# count(): count the occurrences 
data = (10,20,30,40,10,50,10)
print(data)
print(data.count(10)) 

# Lists are Mutable 
pan = ["AKLOP9912Q","MKLOP9912Q",'LOKLOP9912Q']
# Request TO change PAN ID 
pan[1] = "ANLOP9912Q"
print(pan)

# Tuples are Immutable 
PAN_IDS = ("AKLOP9912Q","MKLOP9912Q",'LOKLOP9912Q')
# Request TO change PAN ID 
# pan[1] = "ANLOP9912Q" # TypeError: 'tuple' object does not support item assignment
print(pan)
