# List Methods / Operations On List 

# append(): Adds Element to the end of the list 
data = [10,20,30,40,50]
print(data)
data.append(60)
print(data)

# extend(): add Iterable to the list 
data = [10,20,30,40,50]
print(data)
data.extend([60,70,80])
# data.extend(90) # TypeError: 'int' object is not iterable
print(data)

# insert(): insert data at specific position i.e index 
data = [10,20,40,50]
print(data)
# data.append(30)
data.insert(2,30)
print(data)

data.insert(10,60) # if index is given out of range, add at end
print(data) 

# data.insert(70) # TypeError: insert expected 2 arguments, got 1
# print(data)

# pop(): removes an element, by default the last element 
# if index is provided, removes specific element 
data = [10,20,30,40,50]
print(data)
data.pop()
print(data)

data.pop(0)
print(data)

# data.pop(10) # IndexError: pop index out of range
# print(data)

# remove(): remove element based on value 
data = [10,20,30,40,50]
print(data)
data.remove(30)
print(data)

# data.remove(60) # ValueError: list.remove(x): x not in list
# print(data)

data = [10,20,30,40,10,50,10]
print(data)
data.remove(10)
print(data)

# Requirement: Remove All Occurrences Of 10
data = [10,20,30,40,10,50,10]
print(data)
while 10 in data:
    data.remove(10)
print(data)

# clear(): Empties list 
data = [10,20,30,40,50]
print(data)
data.clear()
print(data)

# index(): Used to get the index position of value 
data = [10,20,30,40,50]
print(data)
print(data.index(20))
# print(data.index(90)) # ValueError: 90 is not in list

# count(): count the occurrences 
data = [10,20,30,40,10,50,10]
print(data)
print(data.count(10))

# reverse(): reverse the list 
data = [10,20,30,40,50]
print(data)
data.reverse()
print(data)

# sort(): sorts the list, default is ascending order
data = [10,30,20,40,50]
print(data)
data.sort()
print(data)

# sort(): sorts the list in descending order
data = [10,30,20,40,50]
print(data)
data.sort(reverse=True)
print(data)

data = ['a','f','b','e']
print(data)
data.sort()
print(data)

data = [10,30,'b','e']
print(data)
# data.sort() # TypeError: '<' not supported between instances of 'str' and 'int'
# print(data)

# copy(): creates a copy of list 
data = [10,30,20,40,50]
print(data)
backup = data.copy()
print(backup)

# product catalog  
product_prices = [99,199,49,299]
product_prices.sort()
print("Prices In Ascending Order: ",product_prices)

# aadhar 
aadhar_ids = [192029202902922,4948400949403,3040409400904]
print(aadhar_ids)

aadhar_ids = [192029202902922,4948400949403,192029202902922]
print(aadhar_ids)

pan = ["AKLOP9912Q","MKLOP9912Q",'LOKLOP9912Q']
# Request TO change PAN ID 
pan[1] = "ANLOP9912Q"
print(pan)
