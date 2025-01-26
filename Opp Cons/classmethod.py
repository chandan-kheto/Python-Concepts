class Person:
    name = "abcd"

    # def changeName(obj,name)
    # self.__class__.name = "Rahul"
    
    @classmethod
    def changeName(cls,name):
        cls.name = name

p1 = Person()
p1.changeName("Rahul kumer")
print(p1.name)
print(Person.name)