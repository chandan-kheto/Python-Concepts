class student:
   def __init__(self,name,marks):
      self.name = name 
      self.marks = marks
      print("adding new student in database...")

s1 = student("karan",98)
print(s1.name, s1.marks)

s2 = student("Ram", 96)
print(s2.name, s2.marks)

