class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f"{self.name} is {self.age} years old.")

person1 = Person("Chirayu", 10)
person2 = Person('Shubhz', +24)

person1.print_info()
person2.print_info()