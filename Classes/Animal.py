from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age, leg_count):
        self.name = name
        self.age = age
        self.leg_count = leg_count

    @abstractmethod
    def to_string(self):
        pass

    @abstractmethod
    def communicate(self):
        pass

    @abstractmethod
    def can_fly(self):
        pass


class Human(Animal):

    def communicate(self):
        return "I am Human, so i can talk"

    def can_fly(self):
        return False

    def to_string(self):
        info = {
            "Name": self.name,
            "Age": self.age,
            "Leg Count": self.leg_count,
            "Communicate":self.communicate(),
            "Can Fly":self.can_fly()
        }
        return info


class Dog(Animal):

    def communicate(self):
        return "I am Dog, so i can bark"

    def can_fly(self):
        return False

    def to_string(self):
        info = {
            "Name": self.name,
            "Age": self.age,
            "Leg Count": self.leg_count,
            "Communicate":self.communicate(),
            "Can Fly":self.can_fly()
        }
        return info


class Cat(Animal):

    def communicate(self):
        return "I am Cat, so i can meow"

    def can_fly(self):
        return False

    def to_string(self):
        info = {
            "Name": self.name,
            "Age": self.age,
            "Leg Count": self.leg_count,
            "Communicate":self.communicate(),
            "Can Fly":self.can_fly()
        }
        return info

class Seagull(Animal):

    def communicate(self):
        return "I am Seagull, so i can huoh-huoh-huoh"

    def can_fly(self):
        return True

    def to_string(self):
        info = {
            "Name": self.name,
            "Age": self.age,
            "Leg Count": self.leg_count,
            "Communicate":self.communicate(),
            "Can Fly":self.can_fly()
        }
        return info
