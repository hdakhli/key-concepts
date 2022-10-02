class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(
            f"I am a cat. My name is {self.name}. "
            f"I am {self.age} years old.")

    def make_sound(self):
        print("Miaou !")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(
            f"I am a dog. My name is {self.name}. "
            f"I am {self.age} years old.")

    def make_sound(self):
        print("Ouaf !")
