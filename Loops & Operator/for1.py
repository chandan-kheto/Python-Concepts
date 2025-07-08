numbers = [5, 10, 15, 20]
total = 0
for num in numbers:
    total += num
print(f"Total sum: {total}") #op: Total sum: 50

print("-----------")

for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} * {j} = {i * j}")
    print("-----------")

