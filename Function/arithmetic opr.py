num1 = float(input("Enter your num1: "))
num2 = float(input("Enter your num2: "))

# addition
def add_num(num1, num2):
  return num1 + num2

# subtraction
def sub_num(num1, num2):
  return num1 - num2

# multiplication
def mul_num(num1, num2):
  return num1 * num2

# division
def div_num(num1, num2):
  return num1 / num2

print("Addition:", add_num(num1, num2))
print("Subtraction:", sub_num(num1, num2))
print("Multiplication:", mul_num(num1, num2))
print("Division:", div_num(num1, num2))