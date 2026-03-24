# Dict Methods / Operations On Dict

data = {"a":"apple","b":"banana"}
print(type(data))

# update(): adds / updates item 
print(data)
data.update({"c":"cherry"}) # if key is not present, then adds  
print(data)
data.update({"a":"apricot"}) # if key is present, then updates  
print(data)

# pop(): remove an item by key 
data = {"a":"apple","b":"banana"}
print(data)
# data.pop() # TypeError: pop expected at least 1 argument, got 0
data.pop("a")
print(data)
# data.pop("c") # KeyError: 'c'
print(data)

# popitem(): removes last item 
data = {"a":"apple","b":"banana"}
print(data)
data.popitem()
print(data)
# data.popitem("a") # TypeError: dict.popitem() takes no arguments (1 given)
print(data)

# clear(): empties dictionary 
data = {"a":"apple","b":"banana"}
print(data)
data.clear()
print(data)

# get(): used to get value for key 
data = {"a":"apple","b":"banana"}
print(data)
# print(data.get()) # TypeError: get expected at least 1 argument, got 0
print(data.get("a"))
print(data.get("c")) # No error with get(), but using data[key] we get error if key is not present

# keys(): used to get keys 
data = {"a":"apple","b":"banana",'c': 'cherry'}
print(data)
print(data.keys()) # set of keys 
# get individual keys 
for key in data.keys():
    print(key)

# values: used to get values
data = {"a":"apple","b":"banana",'c': 'cherry'}
print(data)
print(data.values()) # set of values 
# get individual values 
for value in data.values():
    print(value)
    
# items(): used to get both keys & values 
data = {"a":"apple","b":"banana",'c': 'cherry'}
print(data)
print(data.items()) # set of keys & values 
# get individual item 
for item in data.items():
    print(item)
    
# setdefault(): returns a value of key, if key is already present
# if key not present, then add the item and returns value 
data = {"a":"apple","b":"banana"}
print(data)
data.setdefault("b","blueberry")
out = data.setdefault("b","blueberry")
print(out)
print(data)

data = {"a":"apple","b":"banana"}
print(data)
out = data.setdefault("c","cherry")
print(out)
print(data)

# copy(): create a copy of dict
data = {"a":"apple","b":"banana"}
print(data) 
backup = data.copy()
print(backup) 