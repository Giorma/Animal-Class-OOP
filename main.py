from Classes.Animal import *

human1 = Human("Gio", 18, 2)
dog1 = Dog("Qedana", 5, 4)
cat1 = Cat("kata", 1, 4)
seagull1 = Seagull("tolia", 2, 2)

print(human1.to_string())
print(dog1.to_string())
print(cat1.to_string())
print(seagull1.to_string())

"""
        Output
        
{'Name': 'Gio', 'Age': 18, 'Leg Count': 2, 'Communicate': 'I am Human, so i can talk', 'Can Fly': False}
{'Name': 'Qedana', 'Age': 5, 'Leg Count': 4, 'Communicate': 'I am Dog, so i can bark', 'Can Fly': False}
{'Name': 'kata', 'Age': 1, 'Leg Count': 4, 'Communicate': 'I am Cat, so i can meow', 'Can Fly': False}
{'Name': 'tolia', 'Age': 2, 'Leg Count': 2, 'Communicate': 'I am Seagull, so i can huoh-huoh-huoh', 'Can Fly': True}


"""