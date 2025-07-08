fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")
#op: I like apple, I like banana, I like cherry


print("-----------")

for i in range(5):
    print(i)   #op: 0,1,2,3,4

print("-----------")

for i in range(2, 6):
    print(i)    #op: 2,3,4,5
print("-----------")

for i in range(2, 20, 3):
    print(i)   #op: 2,5,8,11,14,17
print("-----------")

for i in range(6):
    if i == 3:
     continue  # continue: Skips current iteration
    print(i)   #op: 0,1,2,4,5

print("-----------")

for i in range(6):
    if i == 4:
      break # break: Stops loop immediately
    print(i)   #op: 0,1,2,3
