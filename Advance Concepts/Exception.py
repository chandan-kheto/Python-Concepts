try:
  a = int(input("Enter numerator: "))
  b = int(input("Enter denominator: "))
  result = a / b
  print("Result:", result)

except ZeroDivisionError:
    print("You can't divide by zero!")

except ValueError:
    print("Please enter a valid number.")

finally:
    print("Execution complete.")
