# Set Methods / Operations 

# add(): add element to set 
data = {10,20,30,40,50}
print(data)
data.add(60)
print(data)

# update(): add multiple elements to set i.e iterables 
data = {10,20,30,40,50}
print(data)
data.update([60,70,80])
print(data)

# pop(): Removes random element 
data = {10,20,30,40,50}
print(data)
data.pop()
print(data)

# remove(): remove element based on value 
data = {10,20,30,40,50}
print(data)
data.remove(20)
print(data)
# data.remove(90) # KeyError: 90

# discard(): remove element based on value, if not values, no error 
data = {10,20,30,40,50}
print(data)
data.discard(20)
print(data)
data.discard(90)
print(data)

# clear(): empties set 
data = {10,20,30,40,50}
print(data)
data.clear()
print(data)

# copy(): makes a copy 
data = {10,20,30,40,50}
print(data)
backup = data.copy()
print(backup)

# Below Methods will be specific to sets only 
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}

# union(): combine sets 
print(s1.union(s2))
print(s1 | s2)

# intersection(): get common elements from sets 
print(s1.intersection(s2))
print(s1 & s2)
print(s1)
print(s2)

# intersection_update(): get common elements from sets and update calling set
print(s1.intersection_update(s2))
print(s1)
print(s2)

# difference(): remove common elements from the set and gives unique elements 
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.difference(s2))
print(s1 - s2)
print(s1)
print(s2)

# difference_update(): remove common elements from the set and gives unique elements, and update calling set
print(s1.difference_update(s2))
print(s1)
print(s2) 

# symmetric_difference(): remove common elements and takes combined elements from sets 
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.symmetric_difference(s2))
print(s1 ^ s2)
print(s1)
print(s2) 

# symmetric_difference_update(): remove common elements and takes combined elements from sets, and update calling set
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.symmetric_difference_update(s2)) 
print(s1)
print(s2) 

# issubset() : check if a given set is subset or not 
s1 = {10,20,30,40,50}
s2 = {60,70,80}
s3 = {40,50}

print(s1.issubset(s2))
print(s3.issubset(s1))

# issuperset() : check if a given set is superset or not 
s1 = {10,20,30,40,50}
s2 = {60,70,80}
s3 = {40,50}

print(s2.issuperset(s1))
print(s1.issuperset(s3))

# isdisjoint(): checks if sets have no common elements 
s1 = {10,20,30,40,50}
s2 = {60,70,80}
s3 = {40,50}
print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))