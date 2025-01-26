class Car:
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stoped..")

class ToyotoCar(Car):
    def __init__(self,name):
        self.name = name

car1 = ToyotoCar("fortuner")
car2 = ToyotoCar("prius")

print(car1.start())