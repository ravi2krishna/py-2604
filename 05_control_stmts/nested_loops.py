# Nested Loops 

# Generate Math Tables 

# 1 X 1 - 1 X 2 - 1 X 3 - 1 X 4 - 1 X 5 ..........
# 2 X 1 - 2 X 2 - 2 X 3 - 2 X 4 - 2 X 5 ..........
# 3 X 1 - 3 X 2 - 3 X 3 - 3 X 4 - 3 X 5 ..........
# . 
# . 

for outer in range(1,6):
    print(outer)
    print("-------")
    for inner in range(1,6):
        print(inner)
        
# Math Table 
for outer in range(1,6):
    for inner in range(1,6):
       print(f"{outer} * {inner} = {outer * inner}") 
       
# Real world use case for nested loops 
colors = ["black","white","red"]
sizes = ["uk-6","uk-7","uk-8","uk-9","uk-10"]

for color in colors:
    for size in sizes:
        print(color+"----"+size)

outer = 1        
while outer < 6:
    inner = 1
    while inner < 6:
        print(f"{outer} * {inner} = {outer * inner}") 
        inner += 1
    outer += 1