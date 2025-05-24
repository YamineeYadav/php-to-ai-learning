# class Student:
#     def __init__(self,name):
#         self.name = name

# cls = Student("Yaminee Yadav")
# print(cls.name)
# del cls
# print(cls.name)

# private function example
# class Person:
#     __name = "yamini"  # Private variable with double underscores

#     def __hello(self):  # Private method with double underscores
#         print("hello")
#     def welcome(self):
#         self.__hello()
# p1 = Person()

# print(p1.welcome())  # Correct way to call the private method

class Car:
    @staticmethod
    def start():
        print("car started..")
    @staticmethod
    def stop():
        print("car stopped")

class Toyotacar(Car):
    def __init__(self, name):
        self.name = name

car1 = Toyotacar("fortuner")
car2 = Toyotacar("Prius")

car1.start()


