class persion:
    __name = "xyz"

    def __hello(self):
        print("hello persion")
    def welcome(self):
        self.__hello()

p1 = persion()

print(p1.welcome())
