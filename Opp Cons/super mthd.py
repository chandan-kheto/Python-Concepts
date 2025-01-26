class Car:
    def __init__(self,type):
        self.type = type

    @staticmethod
    def start():
        print("car started..")
    @staticmethod
    def stop():
        print("car stopted..")

class ToyotoCar(Car):
    def __init__(self,name,type):
        super().__init__(type)
        super().start()
        self.name = name
car1 = ToyotoCar("prius","electric")
print(car1.type)