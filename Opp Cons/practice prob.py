class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
             sum+= val
        print("Hi", self.name, "Your avg score is:", sum/3)
    
s1 = student("Ram", [99,98,96])
s1.get_avg()

s1.name ="Sama"
s1.get_avg()
